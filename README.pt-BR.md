# mobile-agent-testers

**20 testadores com IA em 20 celulares diferentes, em paralelo, por US$ 0.**

**[Execuções](docs/runs/)** · **[Comparação](docs/compare.md)** · **[Perguntas frequentes](#perguntas-frequentes)** · **[Personas](personas.json)** · **[Versões](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · Português

<sub>Tradução do README em inglês: pode estar atrasada, a referência é o [README.md](README.md).</sub>

Nenhum script de teste para escrever. Cada testador é um agente do Claude Code com seu próprio simulador de iOS
ou emulador de Android no GitHub Actions. Ele interpreta uma persona (iPhone SE em sueco com o maior tamanho de
texto, Pixel 7 a 200%, iPad em alemão, árabe da direita para a esquerda...), usa o seu app como um usuário novo e
escreve um relatório de bugs com capturas de tela. Flutter, React Native, Expo, Kotlin e Swift nativos, Kotlin
Multiplatform, Capacitor e .NET MAUI.

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="Gravações de tela reais de 20 testadores com IA usando o LocalSend ao mesmo tempo: 10 emuladores de Android e 10 simuladores de iOS em 14 idiomas, de um Pixel pequeno a um iPad de 13 polegadas. Quando um testador termina, o celular mostra quantos problemas ele encontrou. Abre o vídeo." width="100%"></a><br>
<sub>Gravações de tela reais da execução no LocalSend, sem os tempos de espera. <a href="assets/localsend-20.mp4">Vídeo completo (MP4)</a> · <a href="docs/runs/localsend-20.md">A execução, aparelho por aparelho</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## Bugs reais encontrados

### LocalSend: 20 agentes, 20 aparelhos, 14 idiomas

<p align="center"><img src="assets/real-findings-localsend-20.png" alt="Quatro telas do LocalSend com as faixas de overflow do Flutter, cada problema marcado em vermelho: um Pixel 7 com texto a 200% em que os seis botões de envio transbordam, um iPhone SE em sueco com o maior tamanho de texto em que o diálogo de mensagem transborda 149 pixels e esconde o campo de texto e o Confirmar, um iPad Air em alemão em que o botão Adicionar sai 114 pixels do cartão, e um iPhone SE em francês com o tamanho de texto padrão em que uma linha transborda 28 pixels" width="100%"></p>

O [LocalSend](https://github.com/localsend/localsend) é um app Flutter com 100 mil estrelas. O que os agentes encontraram:

- iPhone SE em sueco com o maior tamanho de texto do iOS: o diálogo de mensagem transborda 149 px, o campo de texto e o Confirmar ficam fora da tela e não dá para enviar texto.
- Pixel 7 com a fonte do Android a 200%: os seis botões de envio transbordam e cortam os rótulos pela metade. O mesmo num iPhone 16 Plus em italiano no primeiro tamanho de acessibilidade.
- iPad Air em alemão com texto grande: "Hinzufügen" sai 114 px do cartão, e os valores dos Ajustes quebram no meio da palavra.
- iPhone SE em francês com o tamanho de texto padrão: "Recevoir via un lien" transborda 28 px e esconde uma caixa de seleção.
- Pixel Tablet em espanhol: o teclado cobre o Cancelar e o Confirmar do diálogo de endereço.
- Um envio manual que falha diz apenas "Error", "Erreur", "Fehler", "エラー", "Hata" ou "Erro", sem motivo. No iOS, um endereço que não responde deixa o diálogo esperando sem mostrar progresso (três agentes).

103 relatórios no total (1 bloqueador, 15 graves). Agrupados à mão, são 46 bugs distintos, e a maioria foi vista por um único celular:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/bugs-per-phone-dark.svg">
  <img src="assets/bugs-per-phone-light.svg" alt="29 dos 46 bugs do LocalSend foram vistos por um único celular, incluindo o único bloqueador. 6 bugs foram vistos por 2 celulares, 6 por 3, e um cada por 4, 5, 6, 10 e 12 celulares. Nenhum bug foi visto por mais de 12 dos 20." width="100%">
</picture>

69 minutos do início ao último relatório (o plano gratuito roda 5 jobs de macOS ao mesmo tempo), US$ 4,62 de uso do modelo para os 20. Cada relatório, aparelho por aparelho: [docs/runs/localsend-20.md](docs/runs/localsend-20.md). Rode você mesmo:

```bash
gh workflow run agent-testers.yml -f source_repo=localsend/localsend -f app_dir=app \
  -f app_id=org.localsend.localsend_app -f android_personas=all -f ios_personas=all -f record_video=true
```

### AnkiDroid: 10 agentes, direto do APK publicado

<p align="center"><img src="assets/real-findings-ankidroid.png" alt="Quatro telas do AnkiDroid, cada problema marcado em vermelho: um Pixel 7 com texto a 200% em que os botões Again, Hard, Good e Easy aparecem cortados pela metade (ampliado), a página de Estatísticas do mesmo celular em que as linhas saem pela direita, e a tela de boas-vindas em português e em japonês em que o botão Get started continua em inglês" width="100%"></p>

O [AnkiDroid](https://github.com/ankidroid/Anki-Android) é um app Kotlin com 12 mil estrelas. 10 agentes em 10 emuladores de Android, com o APK da versão publicada no GitHub, sem build:

- Pixel 7 com a fonte do Android a 200%: os botões Again / Hard / Good / Easy aparecem cortados pela metade, e o texto das Estatísticas sai pela borda direita. Um segundo agente viu os botões ainda cortados no alfa 2.26, nas duas fileiras quando "Show large answer buttons" está ativado.
- A tela de boas-vindas mostra "Get started" em inglês em aparelhos configurados em português, espanhol e japonês, enquanto o resto da tela está traduzido (três agentes, cada um por conta própria).

83 relatórios, que se agrupam em 43 problemas distintos (dois vêm do WebView do sistema, antigo demais, das imagens de emulador do Android 10 e 11, e não do app). Menos de 10 minutos do início ao último relatório, US$ 4,69 de uso do modelo para os 10. Cada relatório: [docs/runs/ankidroid-10.md](docs/runs/ankidroid-10.md). Rode você mesmo:

```bash
gh workflow run agent-testers.yml -f app_dir=. -f app_id=com.ichi2.anki -f brief=briefs/ankidroid.md \
  -f android_build="curl -fsSL -o anki.apk https://github.com/ankidroid/Anki-Android/releases/download/v2.25.3/AnkiDroid-2.25.3-full-universal.apk" \
  -f apk_path=anki.apk -f android_personas=all -f ios_personas=none -f block_hosts="ankiweb.net www.google-analytics.com"
```

### O exemplo oficial de animações do Flutter

<p align="center"><img src="assets/real-finding-flutter.png" alt="Dois celulares na mesma tela do app de exemplo de animações do Flutter, um Pixel 7 e um iPhone SE em francês, com o título Streamling your courses circulado: os dois agentes relataram esse erro de digitação por conta própria" width="100%"></p>

No [app de exemplo do flutter/packages](https://github.com/flutter/packages/tree/main/packages/animations/example), um agente num Pixel 7 e outro num iPhone SE em francês relataram, cada um, o mesmo erro de digitação, "Streamling your courses" ([linha 110](https://github.com/flutter/packages/blob/main/packages/animations/example/lib/shared_axis_transition.dart#L110)), e o do Android percebeu que o app ignora o modo escuro. 19 minutos, US$ 0,47 de uso do modelo.

Rodou no seu app? [Compartilhe o que ele encontrou](https://github.com/pierridotite/mobile-agent-testers/issues/new?title=Finding:%20) e isso entra nas [execuções](docs/runs/). Se você mantém um desses apps e acha que um bug relatado está errado, abra uma issue: ele é corrigido e a execução é refeita.

## Começo rápido

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # par de chaves + secrets + token do Claude (Windows: .\setup.ps1)
gh workflow run agent-testers.yml     # demo: 2 testadores Android + 2 iOS, ~20 min
bash scripts/collect.sh <run id>      # descriptografa os relatórios e agrupa duplicados: runs/<id>/SUMMARY.md
```

O app de demo tem [11 bugs colocados de propósito](demo-app/BUGS.md). Na execução gravada acima, os 4 testadores da demo encontraram 9 deles (de 2 a 7 minutos por agente, cerca de 21 minutos no total, builds incluídos), além de problemas reais que ninguém colocou (um botão debaixo da barra de navegação do Android, dados que não ficam salvos depois de reabrir). Uso do modelo: US$ 0,87 para os 4.

Ou deixe o Claude configurar para o seu app:

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## Por que não Maestro, Appium ou agent-device?

Eles rodam os testes que você escreve. Estes agentes procuram o que ninguém pensou em testar.

| | mobile-agent-testers | Maestro, Appium, Detox, e2e |
|---|---|---|
| Você escreve | Nada: escolhe personas da lista | Fluxos ou código de teste |
| Ele pega | Layout com texto grande, modo escuro, textos confusos, becos sem saída | O que cada teste verifica |
| Mesmo resultado a cada execução | Não: cada execução explora, então confira as capturas | Sim |

O [agent-device](https://github.com/callstackincubator/agent-device) dá a um agente de programação o controle de um simulador. Este projeto roda uma sessão inteira: faz o build do app, dá a cada persona seu próprio aparelho e junta relatórios criptografados. Use agentes antes de uma versão e fluxos com script para regressões.

Comparação completa, com Firebase Test Lab Robo, mobile-mcp, phonedriver e beta testers humanos: [docs/compare.md](docs/compare.md) (em inglês).

## Teste o seu próprio app

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| Entrada | |
|---|---|
| `source_repo`, `ref` | Repositório e branch do app (vazio = este repositório). Repositório privado: adicione um secret `SOURCE_REPO_TOKEN` somente leitura |
| `app_dir`, `app_id` | Pasta do app, pacote Android / bundle id iOS (se a outra plataforma usa outro id, ele é lido do app compilado) |
| `android_personas`, `ios_personas` | Ids do [personas.json](personas.json), um celular cada, `all`, ou `none` para pular uma plataforma. 20 prontas: 14 idiomas, direita para a esquerda, tablets, texto do pequeno ao maior tamanho de acessibilidade |
| `brief` | Instruções para os agentes ([AGENT_BRIEF.md](AGENT_BRIEF.md)) |
| `framework` | `auto` (padrão) ou force um dos frameworks abaixo |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | Seu próprio comando de build, ou o download de um app já compilado (caminhos relativos a `app_dir`) |
| `block_hosts` | Hosts de analytics bloqueados durante os testes |
| `record_video` | Gravação de tela de cada celular, criptografada com os relatórios |

**Suportados de fábrica** (detecção automática):

| Framework | Android | Simulador de iOS |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| Kotlin / Java, Swift / Objective-C nativos | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | Projeto Xcode do app iOS |
| Capacitor / Ionic | Gradle debug depois de `cap sync` | Xcode depois de `cap sync` |
| .NET MAUI (beta) | `dotnet publish` | `dotnet build` para `iossimulator-arm64` |
| Qualquer outro | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

Os agentes leem a tela pelas capturas e pela árvore de acessibilidade, então qualquer toolkit de interface
funciona. Widgets com rótulo (`Semantics` do Flutter, `contentDescription`, `accessibilityLabel`) dão a eles
toques mais precisos.

## Como funciona

<p align="center"><img src="assets/how-it-works.svg" alt="Como funciona: um workflow faz o build do app, depois um emulador ou simulador com um agente por persona, relatórios criptografados, resumo na sua máquina" width="100%"></p>

- **As personas** definem o aparelho: modelo, sistema, tamanho da fonte, modo escuro, idioma, localização.
- **Três ferramentas por agente**: ver a tela (com coordenadas de toque), gestos, digitação.
- **Verificação de acessibilidade** em cada tela: controles sem nome e áreas de toque menores que 48 dp (Android) ou 44 pt (iOS), que o agente confirma na captura.
- **Resultados criptografados**: os logs de um repositório público são públicos, então tudo é criptografado com a sua chave.
- **Analytics bloqueado** dentro dos celulares, para os testes nunca mexerem nas suas estatísticas reais.
- **Um resumo** na sua máquina: o Claude agrupa os relatórios que descrevem o mesmo bug, então você vê quantas personas encontraram cada um e quais personas encontraram cada tipo de problema.
- **Testes** a cada push, offline e sem celular: verificação de acessibilidade, matriz de personas, resumo, resultados criptografados ([tests/](tests/)).

## Limites

- Os runners do GitHub são gratuitos para repositórios públicos: cerca de 20 jobs ao mesmo tempo, 5 no macOS.
- Em planos com limite de uso a cada 5 horas, 20 agentes podem esgotá-lo em ~15 min: rode lotes de 6 a 10.
- Os runners hospedados são feitos para o projeto do próprio repositório. Para um app de código fechado, rode o workflow no seu repositório privado ou no seu próprio Mac.

## Perguntas frequentes

### 20 agentes não acham o mesmo bug 20 vezes?

Não. No LocalSend, os 103 relatórios eram 46 bugs distintos, e 29 deles foram encontrados por um único agente, incluindo o único bloqueador ([ver a execução](docs/runs/localsend-20.md)). Os bugs de direita para a esquerda só vieram das duas personas em árabe, e os de tablet dos quatro tablets. Os duplicados eram estados do app inteiro que todo mundo encontra, como a lista de aparelhos vazia.

### Quanto custa?

Os runners do GitHub são gratuitos para repositórios públicos, macOS incluído. O uso do modelo foi de US$ 0,15 a US$ 0,55 por agente [nestas execuções](docs/runs/), cerca de US$ 5 para 20 celulares. Com uma assinatura do Claude, as execuções contam no uso do seu plano em vez de virar conta.

### Quanto tempo leva uma execução?

Cada agente explora de 1 a 18 minutos. Os 10 agentes Android do AnkiDroid levaram menos de 10 minutos do início ao último relatório. Os 20 aparelhos do LocalSend levaram 69 minutos, builds incluídos, porque o plano gratuito roda 5 jobs de macOS ao mesmo tempo.

### Preciso de um Mac?

Não. Tudo roda nos runners do GitHub: Linux para Android, macOS para iOS. Você precisa da CLI `gh` e de uma assinatura do Claude ou de uma chave de API, e o `./setup.sh` (`.\setup.ps1` no Windows) faz o resto.

### Duas execuções dão o mesmo resultado?

Não. Cada agente explora, então duas execuções nunca seguem o mesmo caminho: espere os mesmos tipos de bug, não a mesma lista. Mantenha os testes com script (Maestro, Appium) para regressões, veja [a comparação](docs/compare.md).

### Meus relatórios são públicos?

Não. Os logs de um repositório público são públicos, então relatórios, capturas e vídeos são criptografados com a sua chave antes de sair do runner, e só você pode descriptografá-los. Os hosts de analytics são bloqueados dentro dos celulares. Use contas de teste, nunca contas reais. Mais em [PRIVACY.md](PRIVACY.md).

### Posso testar um app de código fechado?

Sim. Rode o workflow a partir de um repositório privado, com um `SOURCE_REPO_TOKEN` somente leitura para o repositório do seu app, ou faça `android_build` e `ios_build` baixarem um APK ou um .app já compilado. Repositórios privados usam os seus minutos do Actions, e os minutos de macOS contam dez vezes.

### Posso criar minhas próprias personas?

Sim. Uma persona são algumas linhas no [personas.json](personas.json): aparelho, versão do sistema, idioma, tamanho do texto, modo escuro, localização, quem ela é e o que tenta fazer.

### Onde ele erra?

Às vezes lê uma tela errado: 3 dos 20 agentes do LocalSend apontaram o teclado em inglês do simulador como parte do app. Alguns minutos por agente cobrem os caminhos principais, não cada canto de um app grande. Cada bug relatado vem com capturas numeradas, então confira antes de abrir qualquer issue.

## Histórico de estrelas

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## Créditos

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

Feito por [@pierridotite](https://github.com/pierridotite) ([LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)) · licença MIT
