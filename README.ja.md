# mobile-agent-testers

**20 人の AI テスターが、20 台の異なるスマートフォンで、同時に、0 ドルで。**

**[実行記録](docs/runs/)** · **[比較](docs/compare.md)** · **[よくある質問](#よくある質問)** · **[ペルソナ](personas.json)** · **[リリース](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [Español](README.es.md) · [Português](README.pt-BR.md)

<sub>このページは英語版の翻訳です。更新が遅れることがあるため、最新の内容は [README.md](README.md) をご覧ください。</sub>

テストスクリプトを書く必要はありません。各テスターは Claude Code のエージェントで、GitHub Actions 上に
自分専用の iOS シミュレーターまたは Android エミュレーターを持ちます。ペルソナ（スウェーデン語で文字サイズ最大の
iPhone SE、フォント 200% の Pixel 7、ドイツ語の iPad、右から左に読むアラビア語……）を演じ、新しいユーザーとして
アプリを使い、スクリーンショット付きのバグレポートを書きます。Flutter、React Native、Expo、ネイティブの Kotlin と
Swift、Kotlin Multiplatform、Capacitor、.NET MAUI に対応しています。

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="20 人の AI テスターが同時に LocalSend を使う実際の画面録画：Android エミュレーター 10 台と iOS シミュレーター 10 台、14 言語、小さな Pixel から 13 インチの iPad まで。テスターが終わると、その端末に見つけた問題の数が表示されます。クリックで動画を開きます。" width="100%"></a><br>
<sub>LocalSend での実行の実際の画面録画（待ち時間はカット）。<a href="assets/localsend-20.mp4">動画全体（MP4）</a> · <a href="docs/runs/localsend-20.md">端末ごとの実行記録</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## 実際に見つかったバグ

### LocalSend：20 エージェント、20 台、14 言語

<p align="center"><img src="assets/real-findings-localsend-20.png" alt="Flutter のオーバーフロー表示が出た LocalSend の 4 画面、問題箇所を赤枠で表示：フォント 200% の Pixel 7 では送信ボタン 6 つがすべてはみ出し、スウェーデン語で文字サイズ最大の iPhone SE ではメッセージのダイアログが 149 ピクセルはみ出して入力欄と確認ボタンが隠れ、ドイツ語の iPad Air では追加ボタンがカードから 114 ピクセルはみ出し、フランス語で標準の文字サイズの iPhone SE では 1 行が 28 ピクセルはみ出している" width="100%"></p>

[LocalSend](https://github.com/localsend/localsend) はスター数 10 万の Flutter アプリです。エージェントが見つけたもの：

- スウェーデン語、iOS の最大の文字サイズの iPhone SE：メッセージのダイアログが 149 px はみ出し、入力欄と「確認」が画面外になるため、テキストを一切送れません。
- Android のフォント 200% の Pixel 7：6 つの送信ボタンがすべてはみ出し、ラベルが半分に切れます。イタリア語で、アクセシビリティの最初のサイズの iPhone 16 Plus でも同じです。
- ドイツ語で大きな文字の iPad Air：「Hinzufügen」がカードから 114 px はみ出し、設定の値が単語の途中で改行されます。
- フランス語で標準の文字サイズの iPhone SE：「Recevoir via un lien」が 28 px はみ出し、チェックボックスが隠れます。
- スペイン語の Pixel Tablet：キーボードがアドレス入力ダイアログの「キャンセル」と「確認」を覆います。
- 手動送信に失敗すると、「Error」「Erreur」「Fehler」「エラー」「Hata」「Erro」としか表示されず、理由がわかりません。iOS では、応答しないアドレスに送るとダイアログが進捗表示もなく待ち続けます（3 つのエージェントがそれぞれ発見）。

レポートは全部で 103 件（ブロッカー 1 件、重大 15 件）。手作業でまとめると 46 個の異なるバグになり、その多くは 1 台の端末でしか見つかっていません：

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/bugs-per-phone-dark.svg">
  <img src="assets/bugs-per-phone-light.svg" alt="LocalSend の 46 個のバグのうち 29 個は 1 台の端末でしか見つからず、唯一のブロッカーもその中に含まれます。2 台で見つかったものが 6 個、3 台が 6 個、4、5、6、10、12 台がそれぞれ 1 個。20 台中 12 台を超えて見つかったバグはありません。" width="100%">
</picture>

開始から最後のレポートまで 69 分（無料プランでは macOS のジョブは同時に 5 つまで）、20 エージェントのモデル使用量は合計 4.62 ドル。すべてのレポートを端末ごとに：[docs/runs/localsend-20.md](docs/runs/localsend-20.md)。自分で実行するには：

```bash
gh workflow run agent-testers.yml -f source_repo=localsend/localsend -f app_dir=app \
  -f app_id=org.localsend.localsend_app -f android_personas=all -f ios_personas=all -f record_video=true
```

### AnkiDroid：10 エージェント、リリース版 APK をそのまま使用

<p align="center"><img src="assets/real-findings-ankidroid.png" alt="AnkiDroid の 4 画面、問題箇所を赤枠で表示：フォント 200% の Pixel 7 で Again、Hard、Good、Easy のボタンが半分に切れている（拡大表示）、同じ端末の統計ページで文字が右端からはみ出している、ポルトガル語と日本語のようこそ画面で Get started ボタンが英語のまま" width="100%"></p>

[AnkiDroid](https://github.com/ankidroid/Anki-Android) はスター数 1.2 万の Kotlin アプリです。10 のエージェントが 10 台の Android エミュレーターで、GitHub のリリースにある APK をそのまま使い、ビルドなしでテストしました：

- Android のフォント 200% の Pixel 7：Again / Hard / Good / Easy のボタンが半分に切れ、統計ページの文字が右端からはみ出します。別のエージェントは、2.26 のアルファ版でもボタンが切れたままで、「Show large answer buttons」をオンにすると 2 段とも切れることを確認しました。
- ポルトガル語、スペイン語、日本語に設定した端末で、ようこそ画面の「Get started」が英語のままです。画面のほかの部分は翻訳されています（3 つのエージェントがそれぞれ発見）。

レポートは 83 件で、43 個の異なる問題にまとまりました（そのうち 2 つは Android 10 と 11 のエミュレーターイメージに入っている古いシステム WebView が原因で、アプリのせいではありません）。開始から最後のレポートまで 10 分未満、10 エージェントのモデル使用量は合計 4.69 ドル。すべてのレポート：[docs/runs/ankidroid-10.md](docs/runs/ankidroid-10.md)。自分で実行するには：

```bash
gh workflow run agent-testers.yml -f app_dir=. -f app_id=com.ichi2.anki -f brief=briefs/ankidroid.md \
  -f android_build="curl -fsSL -o anki.apk https://github.com/ankidroid/Anki-Android/releases/download/v2.25.3/AnkiDroid-2.25.3-full-universal.apk" \
  -f apk_path=anki.apk -f android_personas=all -f ios_personas=none -f block_hosts="ankiweb.net www.google-analytics.com"
```

### Flutter 公式のアニメーションサンプル

<p align="center"><img src="assets/real-finding-flutter.png" alt="Flutter のアニメーションサンプルアプリの同じ画面を表示した 2 台、Pixel 7 とフランス語の iPhone SE。タイトルの Streamling your courses が丸で囲まれている：2 つのエージェントがそれぞれこのタイプミスを報告した" width="100%"></p>

[flutter/packages のサンプルアプリ](https://github.com/flutter/packages/tree/main/packages/animations/example)で、Pixel 7 のエージェントとフランス語の iPhone SE のエージェントが、それぞれ同じタイプミス「Streamling your courses」（[110 行目](https://github.com/flutter/packages/blob/main/packages/animations/example/lib/shared_axis_transition.dart#L110)）を報告し、Android のほうはアプリがダークモードに対応していないことにも気づきました。19 分、モデル使用量 0.47 ドル。

自分のアプリで試しましたか？[見つかったものを共有](https://github.com/pierridotite/mobile-agent-testers/issues/new?title=Finding:%20)してもらえれば、[実行記録](docs/runs/)に加えます。これらのアプリのメンテナーの方で、間違った指摘があると思われる場合は issue を開いてください。修正して実行し直します。

## クイックスタート

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # 鍵ペア + シークレット + Claude トークン（Windows：.\setup.ps1）
gh workflow run agent-testers.yml     # デモ：Android 2 + iOS 2 のテスター、約 20 分
bash scripts/collect.sh <run id>      # レポートを復号して重複をまとめる：runs/<id>/SUMMARY.md
```

デモアプリには[わざと仕込んだバグが 11 個](demo-app/BUGS.md)あります。上で録画した実行では、4 人のデモテスターがそのうち 9 個を見つけ（エージェントごとに 2〜7 分、ビルドを含めて全体で約 21 分）、さらに誰も仕込んでいない本物の問題（Android のナビゲーションバーの下に隠れたボタン、再起動するとデータが残っていない）も見つけました。モデル使用量：4 人で 0.87 ドル。

または、Claude にあなたのアプリ用のセットアップを任せることもできます：

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## Maestro、Appium、agent-device ではだめなの？

それらはあなたが書いたテストを実行します。このエージェントたちは、誰もテストしようと思わなかったところを探します。

| | mobile-agent-testers | Maestro、Appium、Detox、e2e |
|---|---|---|
| 書くもの | なし：一覧からペルソナを選ぶだけ | フローやテストコード |
| 見つけるもの | 大きな文字でのレイアウト、ダークモード、わかりにくい文言、行き止まり | 各テストが確認する内容 |
| 毎回同じ結果か | いいえ：毎回探索するので、スクリーンショットを確認してください | はい |

[agent-device](https://github.com/callstackincubator/agent-device) は、1 つのコーディングエージェントに 1 台のシミュレーターを操作させます。こちらはテストのセッション全体を実行します：アプリをビルドし、ペルソナごとに専用の端末を用意し、暗号化されたレポートを集めます。リリース前にはエージェントを、回帰テストにはスクリプト化したフローを使いましょう。

Firebase Test Lab Robo、mobile-mcp、phonedriver、人間のベータテスターも含めた詳しい比較：[docs/compare.md](docs/compare.md)（英語）。

## 自分のアプリをテストする

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| 入力 | |
|---|---|
| `source_repo`, `ref` | アプリのリポジトリとブランチ（空 = このリポジトリ）。プライベートリポジトリの場合は読み取り専用の `SOURCE_REPO_TOKEN` シークレットを追加 |
| `app_dir`, `app_id` | アプリのフォルダー、Android のパッケージ名 / iOS の bundle id（もう一方のプラットフォームが別の id を使う場合は、ビルドしたアプリから読み取ります） |
| `android_personas`, `ios_personas` | [personas.json](personas.json) の id（1 つにつき 1 台）、`all`、またはプラットフォームを飛ばす `none`。20 人が用意済み：14 言語、右から左、タブレット、小さい文字からアクセシビリティの最大サイズまで |
| `brief` | エージェントへの指示（[AGENT_BRIEF.md](AGENT_BRIEF.md)） |
| `framework` | `auto`（デフォルト）、または下のフレームワークのいずれかを指定 |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | 独自のビルドコマンド、またはビルド済みアプリのダウンロード（パスは `app_dir` からの相対パス） |
| `block_hosts` | テスト中にブロックする分析系のホスト |
| `record_video` | 各端末の画面録画（レポートと一緒に暗号化） |

**そのまま使えるもの**（自動検出）：

| フレームワーク | Android | iOS シミュレーター |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| ネイティブ Kotlin / Java、Swift / Objective-C | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | iOS アプリの Xcode プロジェクト |
| Capacitor / Ionic | `cap sync` 後に Gradle debug | `cap sync` 後に Xcode |
| .NET MAUI（ベータ） | `dotnet publish` | `iossimulator-arm64` 向けの `dotnet build` |
| その他すべて | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

エージェントはスクリーンショットとアクセシビリティツリーから画面を読むので、どの UI ツールキットでも動きます。ラベル付きのウィジェット（Flutter の `Semantics`、`contentDescription`、`accessibilityLabel`）があると、より正確にタップできます。

## 仕組み

<p align="center"><img src="assets/how-it-works.svg" alt="仕組み：1 つのワークフローがアプリをビルドし、ペルソナごとに 1 台のエミュレーターまたはシミュレーターと 1 つのエージェント、暗号化されたレポート、手元のマシンでまとめ" width="100%"></p>

- **ペルソナ**が端末を決めます：機種、OS、文字サイズ、ダークモード、言語、位置情報。
- **エージェントごとに 3 つのツール**：画面を見る（タップ座標付き）、ジェスチャー、文字入力。
- **全画面でアクセシビリティチェック**：名前のないコントロールと、48 dp（Android）または 44 pt（iOS）未満のタップ領域を、エージェントがスクリーンショットで確認します。
- **結果は暗号化**：公開リポジトリのログは公開されるので、すべてあなたの鍵で暗号化します。
- **端末内で分析ツールをブロック**するので、テストが本番の統計に触れることはありません。
- **手元で 1 つのまとめ**：同じバグを指すレポートを Claude がまとめるので、各バグに何人のペルソナが当たったか、どのペルソナがどの種類の問題を見つけたかがわかります。
- **プッシュごとにテスト**（オフライン、スマホ不要）：アクセシビリティチェック、ペルソナの割り当て、まとめ、結果の暗号化（[tests/](tests/)）。

## 制限

- 公開リポジトリでは GitHub のランナーは無料：同時に約 20 ジョブ、そのうち macOS は 5 つ。
- 5 時間ごとの使用量上限があるプランでは、20 エージェントで約 15 分で上限に達します：6〜10 ずつ実行してください。
- ホステッドランナーはそのリポジトリ自身のプロジェクトのためのものです。クローズドソースのアプリは、プライベートリポジトリか自分の Mac でワークフローを実行してください。

## よくある質問

### 20 のエージェントが同じバグを 20 回見つけるだけでは？

いいえ。LocalSend では 103 件のレポートが 46 個の異なるバグにまとまり、そのうち 29 個は 1 つのエージェントしか見つけていません。唯一のブロッカーもその 1 つです（[実行記録](docs/runs/localsend-20.md)）。右から左のバグは 2 人のアラビア語ペルソナだけが、タブレットのバグは 4 台のタブレットだけが見つけました。重複したのは、空のデバイス一覧のように誰もが通るアプリ全体の状態です。

### 費用は？

公開リポジトリでは GitHub のランナーは macOS も含めて無料です。[これまでの実行](docs/runs/)では、モデル使用量はエージェント 1 つあたり 0.15〜0.55 ドルで、20 台でおよそ 5 ドルでした。Claude のサブスクリプションを使う場合は、請求ではなくプランの使用量として数えられます。

### 1 回の実行にかかる時間は？

各エージェントの探索は 1〜18 分です。AnkiDroid の 10 の Android エージェントは、開始から最後のレポートまで 10 分未満でした。LocalSend の 20 台はビルドを含めて 69 分かかりました。無料プランでは macOS のジョブが同時に 5 つまでだからです。

### Mac は必要？

いいえ。すべて GitHub のランナーで動きます：Android は Linux、iOS は macOS です。必要なのは `gh` コマンドと、Claude のサブスクリプションまたは API キーだけで、あとは `./setup.sh`（Windows では `.\setup.ps1`）がやってくれます。

### 2 回実行すると同じ結果になる？

なりません。各エージェントは探索するので、2 回の実行が同じ道をたどることはありません。同じ種類のバグは見つかりますが、同じリストにはなりません。回帰テストにはスクリプト化したテスト（Maestro、Appium）を使い続けてください。[比較](docs/compare.md)もどうぞ。

### レポートは公開される？

いいえ。公開リポジトリのログは公開されるので、レポート、スクリーンショット、動画はランナーを出る前にあなたの鍵で暗号化され、復号できるのはあなただけです。分析系のホストは端末内でブロックされます。本物のアカウントではなく、必ずテスト用アカウントを使ってください。詳しくは [PRIVACY.md](PRIVACY.md)。

### クローズドソースのアプリもテストできる？

できます。プライベートリポジトリからワークフローを実行し、読み取り専用の `SOURCE_REPO_TOKEN` でアプリのリポジトリを読み込むか、`android_build` と `ios_build` でビルド済みの APK や .app をダウンロードします。プライベートリポジトリでは Actions の利用時間を消費し、macOS の時間は 10 倍で数えられます。

### 自分でペルソナを作れる？

作れます。ペルソナは [personas.json](personas.json) の数行です：端末、OS のバージョン、言語、文字サイズ、ダークモード、位置情報、どんな人で何をしようとしているか。

### 苦手なことは？

画面を読み違えることがあります：LocalSend では 20 のエージェントのうち 3 つが、シミュレーターの英語キーボードをアプリの一部だと報告しました。エージェントごとの探索は数分なので、主な操作の流れはカバーしても、大きなアプリの隅々まではカバーしません。どの指摘にも番号付きのスクリーンショットが付くので、報告する前に確認してください。

## スターの推移

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## クレジット

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

作者：[@pierridotite](https://github.com/pierridotite)（[LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)）· MIT ライセンス
