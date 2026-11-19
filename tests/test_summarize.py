"""scripts/summarize.py: merges every persona's findings.json into SUMMARY.md."""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import summarize  # noqa: E402

FINDINGS = {
    "anna": {"score": 6, "issues": [
        {"title": "Send button cut at large text", "severity": "major", "screen": "Send"},
        {"title": "Icon buttons have no name", "severity": "minor", "screen": "Home"}]},
    "noah": {"score": 8, "issues": [
        {"title": "send button cut at large text", "severity": "minor", "screen": "Send"},
        {"title": "App crashes on rotate | landscape", "severity": "blocker", "screen": "Home"}]},
    "kenji": {"score": 7, "issues": [
        {"title": "Icon buttons have no name", "severity": "minor", "screen": "Settings"}]},
}


def write_run(base, findings):
    """Same layout as a decrypted run: <persona>/results/<persona>/findings.json"""
    for persona, data in findings.items():
        d = Path(base, persona, "results", persona)
        d.mkdir(parents=True)
        (d / "findings.json").write_text(json.dumps(data) if isinstance(data, dict) else data, encoding="utf-8")


class Summary(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        write_run(self.tmp.name, FINDINGS)
        self.findings, self.scores = summarize.load(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_load_reads_every_persona(self):
        self.assertEqual(len(self.findings), 5)
        self.assertEqual(sorted(self.scores), [6, 7, 8])
        self.assertEqual({f["persona"] for f in self.findings}, {"anna", "noah", "kenji"})

    def test_broken_findings_file_is_skipped(self):
        write_run(self.tmp.name, {"olga": "{not json"})
        self.assertEqual(len(summarize.load(self.tmp.name)[0]), 5)

    def test_identical_titles_merge_whatever_the_case(self):
        groups = summarize.group_by_title(self.findings)
        self.assertEqual(sorted(len(g["ids"]) for g in groups), [1, 2, 2])

    def test_most_severe_first_then_most_personas(self):
        md = summarize.render(self.findings, self.scores, summarize.group_by_title(self.findings), False)
        table = [line for line in md.splitlines() if line.startswith("| ") and "Severity" not in line]
        self.assertTrue(table[0].startswith("| blocker | App crashes on rotate \\| landscape"))
        self.assertTrue(table[1].startswith("| major | Send button cut at large text | 2 (anna, noah)"))
        self.assertIn("5 reports from 3 personas, average score 7.0/10.", md)

    def test_no_claude_call_when_grouping_is_off(self):
        with mock.patch.dict(os.environ, {"SUMMARY_GROUPING": "0"}), mock.patch.object(summarize.subprocess, "run") as run:
            self.assertIsNone(summarize.group_with_claude(self.findings))
            run.assert_not_called()

    def test_claude_answer_is_checked_before_use(self):
        # ids follow persona order: anna 1-2, kenji 3, noah 4-5
        answer = {"groups": [
            {"title": "Send button cut", "class": "layout and text size", "ids": [1, "4", 99]},
            {"title": "Icon buttons with no name", "class": "made-up class", "ids": [4, 2, 3]},
            "not a group"]}
        reply = mock.Mock(stdout=json.dumps({"result": "Here:\n" + json.dumps(answer)}))
        with mock.patch.dict(os.environ, {"SUMMARY_GROUPING": "1"}), \
                mock.patch.object(summarize.shutil, "which", return_value="/usr/bin/claude"), \
                mock.patch.object(summarize.subprocess, "run", return_value=reply), \
                contextlib.redirect_stderr(io.StringIO()):
            groups = summarize.group_with_claude(self.findings)
        # unknown id dropped, an id used twice kept once, unknown class emptied
        self.assertEqual(groups[0], {"title": "Send button cut", "class": "layout and text size", "ids": [1, 4]})
        self.assertEqual(groups[1], {"title": "Icon buttons with no name", "class": "", "ids": [2, 3]})
        self.assertEqual([g["ids"] for g in groups[2:]], [[5]])  # a report Claude forgot stays, alone

    def test_unusable_claude_answer_falls_back_to_titles(self):
        with mock.patch.dict(os.environ, {"SUMMARY_GROUPING": "1"}), \
                mock.patch.object(summarize.shutil, "which", return_value="/usr/bin/claude"), \
                mock.patch.object(summarize.subprocess, "run", return_value=mock.Mock(stdout="usage limit")), \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertIsNone(summarize.group_with_claude(self.findings))

    def test_command_line(self):
        out = subprocess.run([sys.executable, str(ROOT / "scripts/summarize.py"), self.tmp.name],
                             env=dict(os.environ, SUMMARY_GROUPING="0"), capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertTrue(out.stdout.startswith("# Agent test summary\n"))
        self.assertIn("install the claude CLI", out.stdout)


if __name__ == "__main__":
    unittest.main()
