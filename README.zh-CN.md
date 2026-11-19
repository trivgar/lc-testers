# mobile-agent-testers

**20 个 AI 测试员，20 台不同的手机，并行运行，花费 0 美元。**

**[运行记录](docs/runs/)** · **[对比](docs/compare.md)** · **[常见问题](#常见问题)** · **[角色](personas.json)** · **[版本](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · 简体中文 · [日本語](README.ja.md) · [Español](README.es.md) · [Português](README.pt-BR.md)

<sub>本页译自英文版，可能稍有滞后，以 [README.md](README.md) 为准。</sub>

无需编写测试脚本。每个测试员都是一个 Claude Code 智能体，在 GitHub Actions 上拥有自己的 iOS
模拟器或 Android 模拟器。它扮演一个角色（瑞典语、最大字号的 iPhone SE，字体 200% 的 Pixel 7，
德语 iPad，从右到左的阿拉伯语……），像新用户一样使用你的应用，并写出带截图的缺陷报告。
支持 Flutter、React Native、Expo、原生 Kotlin 和 Swift、Kotlin Multiplatform、Capacitor 和 .NET MAUI。

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="20 个 AI 测试员同时使用 LocalSend 的真实录屏：10 台 Android 模拟器和 10 台 iOS 模拟器，14 种语言，从小屏 Pixel 到 13 英寸 iPad。测试员完成后，手机上会显示它发现的问题数量。点击打开视频。" width="100%"></a><br>
<sub>LocalSend 那次运行的真实录屏，已剪掉空闲时间。<a href="assets/localsend-20.mp4">完整视频（MP4）</a> · <a href="docs/runs/localsend-20.md">逐台设备查看这次运行</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## 真实发现

### LocalSend：20 个智能体，20 台设备，14 种语言

<p align="center"><img src="assets/real-findings-localsend-20.png" alt="四个带有 Flutter 溢出条纹的 LocalSend 界面，问题处用红框标出：字体 200% 的 Pixel 7 上六个发送按钮全部溢出；瑞典语、最大字号的 iPhone SE 上消息对话框溢出 149 像素，挡住了输入框和确认按钮；德语 iPad Air 上添加按钮超出卡片 114 像素；法语、默认字号的 iPhone SE 上一行溢出 28 像素" width="100%"></p>

[LocalSend](https://github.com/localsend/localsend) 是一个 10 万星的 Flutter 应用。智能体发现了：

- 瑞典语、iOS 最大字号的 iPhone SE：消息对话框溢出 149 px，输入框和“确认”按钮都在屏幕外，根本无法发送文字。
- Android 字体 200% 的 Pixel 7：六个“发送”按钮全部溢出，标签被切掉一半。意大利语、第一档辅助功能字号的 iPhone 16 Plus 上也一样。
- 德语、大字号的 iPad Air：“Hinzufügen”超出卡片 114 px，设置里的值在单词中间断行。
- 法语、默认字号的 iPhone SE：“Recevoir via un lien”溢出 28 px，挡住了一个复选框。
- 西班牙语的 Pixel Tablet：键盘挡住了地址对话框的“取消”和“确认”。
- 手动发送失败时只显示“Error”“Erreur”“Fehler”“エラー”“Hata”或“Erro”，不给任何原因。在 iOS 上，地址没有响应时对话框会一直等待，看不到任何进度（三个智能体各自发现）。

共 103 份报告（1 个阻断级，15 个严重）。人工归并后是 46 个不同的缺陷，其中大多数只被一台手机发现：

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/bugs-per-phone-dark.svg">
  <img src="assets/bugs-per-phone-light.svg" alt="LocalSend 的 46 个缺陷中有 29 个只被一台手机发现，其中包括唯一的阻断级缺陷。6 个被 2 台手机发现，6 个被 3 台发现，4、5、6、10 和 12 台手机各发现 1 个。没有任何缺陷被超过 20 台中的 12 台发现。" width="100%">
</picture>

从开始到最后一份报告用时 69 分钟（免费计划同时只能运行 5 个 macOS 任务），20 个智能体的模型用量共 4.62 美元。每份报告、每台设备：[docs/runs/localsend-20.md](docs/runs/localsend-20.md)。自己运行：

```bash
gh workflow run agent-testers.yml -f source_repo=localsend/localsend -f app_dir=app \
  -f app_id=org.localsend.localsend_app -f android_personas=all -f ios_personas=all -f record_video=true
```

### AnkiDroid：10 个智能体，直接使用发布版 APK

<p align="center"><img src="assets/real-findings-ankidroid.png" alt="四个 AnkiDroid 界面，问题处用红框标出：字体 200% 的 Pixel 7 上 Again、Hard、Good、Easy 按钮被切掉一半（放大显示），同一台手机的统计页文字超出右边缘，以及葡萄牙语和日语的欢迎页上 Get started 按钮仍是英文" width="100%"></p>

[AnkiDroid](https://github.com/ankidroid/Anki-Android) 是一个 1.2 万星的 Kotlin 应用。10 个智能体在 10 台 Android 模拟器上，直接使用其 GitHub 发布页上的 APK，无需构建：

- Android 字体 200% 的 Pixel 7：Again / Hard / Good / Easy 按钮被切掉一半，统计页的文字超出右边缘。另一个智能体发现 2.26 alpha 上按钮依然被截断，打开“Show large answer buttons”后两排都是如此。
- 在设为葡萄牙语、西班牙语和日语的设备上，欢迎页的“Get started”仍是英文，而页面其余部分都已翻译（三个智能体各自发现）。

83 份报告，归并为 43 个不同的问题（其中两个来自 Android 10 和 11 模拟器镜像里过旧的系统 WebView，与应用无关）。从开始到最后一份报告不到 10 分钟，10 个智能体的模型用量共 4.69 美元。每份报告：[docs/runs/ankidroid-10.md](docs/runs/ankidroid-10.md)。自己运行：

```bash
gh workflow run agent-testers.yml -f app_dir=. -f app_id=com.ichi2.anki -f brief=briefs/ankidroid.md \
  -f android_build="curl -fsSL -o anki.apk https://github.com/ankidroid/Anki-Android/releases/download/v2.25.3/AnkiDroid-2.25.3-full-universal.apk" \
  -f apk_path=anki.apk -f android_personas=all -f ios_personas=none -f block_hosts="ankiweb.net www.google-analytics.com"
```

### Flutter 官方动画示例

<p align="center"><img src="assets/real-finding-flutter.png" alt="Flutter 动画示例应用同一界面的两台手机：Pixel 7 和法语 iPhone SE，标题 Streamling your courses 被圈出：两个智能体各自报告了这个拼写错误" width="100%"></p>

在 [flutter/packages 的示例应用](https://github.com/flutter/packages/tree/main/packages/animations/example)中，Pixel 7 上的一个智能体和法语 iPhone SE 上的另一个智能体各自报告了同一个拼写错误“Streamling your courses”（[第 110 行](https://github.com/flutter/packages/blob/main/packages/animations/example/lib/shared_axis_transition.dart#L110)），Android 上的那个还注意到应用不支持深色模式。用时 19 分钟，模型用量 0.47 美元。

在你的应用上跑过了？[分享它的发现](https://github.com/pierridotite/mobile-agent-testers/issues/new?title=Finding:%20)，它会被加入[运行记录](docs/runs/)。如果你维护其中某个应用，并认为某个发现有误，请提 issue，我们会修正并重新运行。

## 快速开始

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # 密钥对 + secrets + Claude 令牌（Windows：.\setup.ps1）
gh workflow run agent-testers.yml     # 演示：2 个 Android + 2 个 iOS 测试员，约 20 分钟
bash scripts/collect.sh <run id>      # 解密报告并归并重复项：runs/<id>/SUMMARY.md
```

演示应用里有 [11 个故意埋下的缺陷](demo-app/BUGS.md)。在上面录制的那次运行中，4 个演示测试员找到了其中 9 个（每个智能体 2 到 7 分钟，整次运行约 21 分钟，含构建），还发现了没人埋下的真实问题（一个按钮被 Android 导航栏挡住、重新启动后数据没有保留）。模型用量：4 个共 0.87 美元。

或者让 Claude 为你的应用完成设置：

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## 为什么不用 Maestro、Appium 或 agent-device？

它们运行你写好的测试。这些智能体寻找没人想到要测的东西。

| | mobile-agent-testers | Maestro、Appium、Detox、e2e |
|---|---|---|
| 你要写的 | 什么都不用：从列表里选角色 | 流程或测试代码 |
| 能发现 | 大字号下的布局、深色模式、令人困惑的文案、死胡同 | 每个测试所检查的内容 |
| 每次结果相同 | 否：每次都在探索，所以请查看截图 | 是 |

[agent-device](https://github.com/callstackincubator/agent-device) 让一个编程智能体操作一台模拟器。本项目运行完整的测试会话：构建应用，给每个角色分配自己的设备，并收集加密的报告。发布前用智能体，回归测试用脚本化流程。

完整对比，包括 Firebase Test Lab Robo、mobile-mcp、phonedriver 和真人 Beta 测试员：[docs/compare.md](docs/compare.md)（英文）。

## 测试你自己的应用

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| 输入 | |
|---|---|
| `source_repo`, `ref` | 应用仓库和分支（留空 = 本仓库）。私有仓库：添加一个只读的 `SOURCE_REPO_TOKEN` secret |
| `app_dir`, `app_id` | 应用目录，Android 包名 / iOS bundle id（如果另一个平台用的是别的 id，会从它的构建产物中读取） |
| `android_personas`, `ios_personas` | [personas.json](personas.json) 中的 id，每个角色一台手机；`all` 表示全部，`none` 表示跳过该平台。内置 20 个角色：14 种语言、从右到左、平板、从小号到最大辅助功能字号 |
| `brief` | 给智能体的说明（[AGENT_BRIEF.md](AGENT_BRIEF.md)） |
| `framework` | `auto`（默认），或强制使用下表中的某个框架 |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | 你自己的构建命令，或下载一个预构建的应用（路径相对于 `app_dir`） |
| `block_hosts` | 测试期间屏蔽的统计分析域名 |
| `record_video` | 每台手机的录屏，与报告一起加密 |

**开箱即用**（自动检测）：

| 框架 | Android | iOS 模拟器 |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| 原生 Kotlin / Java、Swift / Objective-C | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | iOS 应用的 Xcode 工程 |
| Capacitor / Ionic | `cap sync` 后 Gradle debug | `cap sync` 后 Xcode |
| .NET MAUI（测试版） | `dotnet publish` | 针对 `iossimulator-arm64` 的 `dotnet build` |
| 其他任何框架 | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

智能体通过截图和无障碍树读取屏幕，所以任何 UI 工具包都适用。带标签的控件（Flutter `Semantics`、`contentDescription`、`accessibilityLabel`）能让它们点得更准。

## 工作原理

<p align="center"><img src="assets/how-it-works.svg" alt="工作原理：一个工作流构建应用，然后每个角色一台模拟器和一个智能体，报告加密，汇总在你的电脑上生成" width="100%"></p>

- **角色**决定设备：型号、系统版本、字号、深色模式、语言、位置。
- **每个智能体三个工具**：查看屏幕（带点击坐标）、手势、输入文字。
- **每个屏幕都做无障碍检查**：没有名称的控件，以及小于 48 dp（Android）或 44 pt（iOS）的触控目标，由智能体在截图上确认。
- **结果加密**：公开仓库的日志是公开的，所以一切都用你的密钥加密。
- **手机内屏蔽统计分析**，测试不会碰到你的真实数据。
- **在你的电脑上生成一份汇总**：Claude 把描述同一缺陷的报告归并起来，你能看到每个缺陷被多少个角色遇到，以及哪些角色发现了哪类问题。
- **每次推送都会测试**，离线、无需手机：无障碍检查、角色矩阵、汇总、加密结果（[tests/](tests/)）。

## 限制

- 公开仓库的 GitHub runner 免费：同时约 20 个任务，其中 macOS 5 个。
- 对于有 5 小时用量上限的套餐，20 个智能体大约 15 分钟就能用完：每批运行 6 到 10 个。
- 托管 runner 应该用于仓库自身的项目。闭源应用请在你的私有仓库或自己的 Mac 上运行这个工作流。

## 常见问题

### 20 个智能体会不会把同一个缺陷找 20 遍？

不会。在 LocalSend 上，103 份报告对应 46 个不同的缺陷，其中 29 个只被一个智能体发现，包括唯一的阻断级缺陷（[见这次运行](docs/runs/localsend-20.md)）。从右到左的缺陷只来自两个阿拉伯语角色，平板的缺陷只来自四台平板。重复的都是人人都会遇到的全局状态，比如空的设备列表。

### 要花多少钱？

公开仓库的 GitHub runner 免费，包括 macOS。在[这些运行](docs/runs/)中，每个智能体的模型用量为 0.15 到 0.55 美元，20 台手机大约 5 美元。如果使用 Claude 订阅，运行会计入你套餐的用量，不会另外收费。

### 一次运行要多久？

每个智能体探索 1 到 18 分钟。AnkiDroid 的 10 个 Android 智能体从开始到最后一份报告不到 10 分钟。LocalSend 的 20 台设备用了 69 分钟（含构建），因为免费计划同时只能运行 5 个 macOS 任务。

### 需要 Mac 吗？

不需要。一切都在 GitHub 的 runner 上运行：Android 用 Linux，iOS 用 macOS。你只需要 `gh` 命令行工具，以及 Claude 订阅或 API 密钥，其余的交给 `./setup.sh`（Windows 上是 `.\setup.ps1`）。

### 两次运行的结果会一样吗？

不会。每个智能体都在探索，两次运行不会走同一条路：会发现同类的缺陷，但不是同一份清单。回归测试请继续使用脚本化测试（Maestro、Appium），参见[对比](docs/compare.md)。

### 我的报告是公开的吗？

不是。公开仓库的日志是公开的，所以报告、截图和视频在离开 runner 之前就已用你的密钥加密，只有你能解密。手机内会屏蔽统计分析域名。请使用测试账号，不要用真实账号。详见 [PRIVACY.md](PRIVACY.md)。

### 可以测试闭源应用吗？

可以。在私有仓库中运行这个工作流，用只读的 `SOURCE_REPO_TOKEN` 访问你的应用仓库，或者让 `android_build` 和 `ios_build` 下载预构建的 APK 或 .app。私有仓库会消耗你的 Actions 分钟数，macOS 的分钟按十倍计算。

### 可以自己定义角色吗？

可以。一个角色就是 [personas.json](personas.json) 里的几行：设备、系统版本、语言、字号、深色模式、位置、这个人是谁，以及想做什么。

### 它会出什么错？

它有时会看错屏幕：LocalSend 的 20 个智能体中有 3 个把模拟器的英文键盘当成了应用的一部分。每个智能体只探索几分钟，覆盖主要路径，而不是大型应用的每个角落。每个发现都附带编号截图，提交之前请先核对。

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## 致谢

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

由 [@pierridotite](https://github.com/pierridotite) 制作（[LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)）· MIT 许可证
