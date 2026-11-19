# Changelog

## Unreleased

- **Standalone skill**: `skills/mobile-agent-testers/` is the plugin's setup skill as a plain Agent Skill, for skill catalogs and agents without Claude Code plugins. A test keeps the two copies identical.

## 0.1.0 (19 November 2026)

The first tagged version: everything behind the [LocalSend, AnkiDroid and Flutter runs](docs/runs/).

- **One workflow** builds your app (Flutter, React Native, Expo, native Kotlin and Swift, Kotlin Multiplatform, Capacitor, .NET MAUI) or downloads a prebuilt APK or .app, then gives each persona its own Android emulator or iOS Simulator on GitHub Actions.
- **20 ready-made personas**: 14 languages, right to left, tablets, Android 10 to 15, text from small to iOS's largest accessibility size. `all` runs them all, `none` skips a platform.
- **Accessibility check** on every screen the agents read: controls with no name and touch targets under 48 dp (Android) or 44 pt (iOS).
- **Encrypted results**: reports, screenshots, build logs and optional screen recordings (`record_video`) are encrypted with your public key before upload. Analytics hosts are blocked inside the phones.
- **One summary**: `scripts/collect.sh <run id>` decrypts everything and groups the reports that describe the same bug into `runs/<id>/SUMMARY.md`.
- **Tests** run offline on every push, on Python 3.9 and 3.13: accessibility check, persona matrix, `personas.json`, summary, and the encrypted results path from the runner to `collect.sh`.
- **Public app repos** need no token; private ones take a read-only `SOURCE_REPO_TOKEN`.
- **Claude Code plugin**: `/plugin marketplace add pierridotite/mobile-agent-testers` sets it up for your app.

Already made a copy from the template? Take `.github/workflows/agent-testers.yml`, `scripts/`, `AGENT_BRIEF.md` and `personas.json` from this version.
