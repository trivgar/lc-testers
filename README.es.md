# mobile-agent-testers

**20 testers con IA en 20 teléfonos distintos, en paralelo, por 0 $.**

**[Ejecuciones](docs/runs/)** · **[Comparativa](docs/compare.md)** · **[Preguntas frecuentes](#preguntas-frecuentes)** · **[Personas](personas.json)** · **[Versiones](https://github.com/pierridotite/mobile-agent-testers/releases)**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · Español · [Português](README.pt-BR.md)

<sub>Traducción del README en inglés: puede ir con retraso, la referencia es [README.md](README.md).</sub>

Sin scripts de prueba que escribir. Cada tester es un agente de Claude Code con su propio simulador de iOS
o emulador de Android en GitHub Actions. Interpreta una persona (iPhone SE en sueco con el texto más grande,
Pixel 7 al 200 %, iPad en alemán, árabe de derecha a izquierda...), usa tu app como un usuario nuevo y escribe
un informe de errores con capturas. Flutter, React Native, Expo, Kotlin y Swift nativos, Kotlin
Multiplatform, Capacitor y .NET MAUI.

<p align="center"><a href="assets/localsend-20.mp4"><img src="assets/localsend-20.gif" alt="Grabaciones de pantalla reales de 20 testers con IA usando LocalSend a la vez: 10 emuladores de Android y 10 simuladores de iOS en 14 idiomas, desde un Pixel pequeño hasta un iPad de 13 pulgadas. Cuando un tester termina, su teléfono muestra cuántos problemas encontró. Abre el vídeo." width="100%"></a><br>
<sub>Grabaciones de pantalla reales de la ejecución en LocalSend, sin los tiempos muertos. <a href="assets/localsend-20.mp4">Vídeo completo (MP4)</a> · <a href="docs/runs/localsend-20.md">La ejecución, dispositivo por dispositivo</a></sub></p>

[![Tests](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml/badge.svg)](https://github.com/pierridotite/mobile-agent-testers/actions/workflows/tests.yml)
[![Stars](https://img.shields.io/github/stars/pierridotite/mobile-agent-testers?style=flat)](https://github.com/pierridotite/mobile-agent-testers/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![iOS + Android](https://img.shields.io/badge/platforms-iOS%20%2B%20Android-blue)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange)
[![Last commit](https://img.shields.io/github/last-commit/pierridotite/mobile-agent-testers)](https://github.com/pierridotite/mobile-agent-testers/commits/main)

## Hallazgos reales

### LocalSend: 20 agentes, 20 dispositivos, 14 idiomas

<p align="center"><img src="assets/real-findings-localsend-20.png" alt="Cuatro pantallas de LocalSend con las franjas de desbordamiento de Flutter, cada problema enmarcado en rojo: un Pixel 7 con el texto al 200 % donde los seis botones de envío se desbordan, un iPhone SE en sueco con el texto más grande donde el diálogo de mensaje se desborda 149 píxeles y oculta el campo de texto y Confirmar, un iPad Air en alemán donde el botón Añadir se sale 114 píxeles de su tarjeta, y un iPhone SE en francés con el tamaño de texto por defecto donde una fila se desborda 28 píxeles" width="100%"></p>

[LocalSend](https://github.com/localsend/localsend) es una app de Flutter con 100 000 estrellas. Lo que encontraron los agentes:

- iPhone SE en sueco con el texto más grande de iOS: el diálogo de mensaje se desborda 149 px, el campo de texto y Confirmar quedan fuera de la pantalla y no se puede enviar texto.
- Pixel 7 con la fuente de Android al 200 %: los seis botones de envío se desbordan y cortan sus etiquetas por la mitad. Lo mismo en un iPhone 16 Plus en italiano con el primer tamaño de accesibilidad.
- iPad Air en alemán con texto grande: «Hinzufügen» se sale 114 px de su tarjeta, y los valores de Ajustes se parten a mitad de palabra.
- iPhone SE en francés con el tamaño de texto por defecto: «Recevoir via un lien» se desborda 28 px y oculta una casilla.
- Pixel Tablet en español: el teclado tapa Cancelar y Confirmar en el diálogo de dirección.
- Un envío manual fallido solo dice «Error», «Erreur», «Fehler», «エラー», «Hata» o «Erro», sin motivo. En iOS, una dirección que no responde deja el diálogo esperando sin mostrar progreso (tres agentes).

103 informes en total (1 bloqueante, 15 graves). Agrupados a mano son 46 errores distintos, y la mayoría los vio un solo teléfono:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/bugs-per-phone-dark.svg">
  <img src="assets/bugs-per-phone-light.svg" alt="29 de los 46 errores de LocalSend los vio un solo teléfono, incluido el único bloqueante. 6 errores los vieron 2 teléfonos, 6 los vieron 3, y uno cada uno 4, 5, 6, 10 y 12 teléfonos. Ningún error lo vieron más de 12 de los 20." width="100%">
</picture>

69 minutos desde el inicio hasta el último informe (el plan gratuito ejecuta 5 trabajos de macOS a la vez), 4,62 $ de uso del modelo para los 20. Cada informe, dispositivo por dispositivo: [docs/runs/localsend-20.md](docs/runs/localsend-20.md). Ejecútalo tú mismo:

```bash
gh workflow run agent-testers.yml -f source_repo=localsend/localsend -f app_dir=app \
  -f app_id=org.localsend.localsend_app -f android_personas=all -f ios_personas=all -f record_video=true
```

### AnkiDroid: 10 agentes, directamente con el APK publicado

<p align="center"><img src="assets/real-findings-ankidroid.png" alt="Cuatro pantallas de AnkiDroid, cada problema enmarcado en rojo: un Pixel 7 con el texto al 200 % donde los botones Again, Hard, Good y Easy se cortan por la mitad (ampliado), la página de Estadísticas del mismo teléfono donde las líneas se salen por la derecha, y la pantalla de bienvenida en portugués y en japonés donde el botón Get started sigue en inglés" width="100%"></p>

[AnkiDroid](https://github.com/ankidroid/Anki-Android) es una app de Kotlin con 12 000 estrellas. 10 agentes en 10 emuladores de Android, con el APK de su versión en GitHub, sin compilar nada:

- Pixel 7 con la fuente de Android al 200 %: los botones Again / Hard / Good / Easy se cortan por la mitad, y el texto de Estadísticas se sale por la derecha. Un segundo agente vio los botones todavía cortados en su alfa 2.26, en las dos filas cuando «Show large answer buttons» está activado.
- La pantalla de bienvenida dice «Get started» en inglés en dispositivos en portugués, español y japonés, mientras el resto de la pantalla está traducido (tres agentes, cada uno por su cuenta).

83 informes, que se agrupan en 43 problemas distintos (dos vienen del WebView del sistema, demasiado antiguo, de las imágenes de emulador de Android 10 y 11, no de la app). Menos de 10 minutos desde el inicio hasta el último informe, 4,69 $ de uso del modelo para los 10. Cada informe: [docs/runs/ankidroid-10.md](docs/runs/ankidroid-10.md). Ejecútalo tú mismo:

```bash
gh workflow run agent-testers.yml -f app_dir=. -f app_id=com.ichi2.anki -f brief=briefs/ankidroid.md \
  -f android_build="curl -fsSL -o anki.apk https://github.com/ankidroid/Anki-Android/releases/download/v2.25.3/AnkiDroid-2.25.3-full-universal.apk" \
  -f apk_path=anki.apk -f android_personas=all -f ios_personas=none -f block_hosts="ankiweb.net www.google-analytics.com"
```

### El ejemplo oficial de animaciones de Flutter

<p align="center"><img src="assets/real-finding-flutter.png" alt="Dos teléfonos en la misma pantalla de la app de ejemplo de animaciones de Flutter, un Pixel 7 y un iPhone SE en francés, con el título Streamling your courses rodeado: los dos agentes informaron de esta errata por su cuenta" width="100%"></p>

En la [app de ejemplo de flutter/packages](https://github.com/flutter/packages/tree/main/packages/animations/example), un agente en un Pixel 7 y otro en un iPhone SE en francés informaron cada uno de la misma errata, «Streamling your courses» ([línea 110](https://github.com/flutter/packages/blob/main/packages/animations/example/lib/shared_axis_transition.dart#L110)), y el de Android notó que la app ignora el modo oscuro. 19 minutos, 0,47 $ de uso del modelo.

¿Lo has probado en tu app? [Comparte lo que encontró](https://github.com/pierridotite/mobile-agent-testers/issues/new?title=Finding:%20) y entrará en [las ejecuciones](docs/runs/). Si mantienes una de estas apps y crees que un hallazgo es erróneo, abre un issue: se corrige y se vuelve a ejecutar.

## Inicio rápido

```bash
gh repo create my-testers --public --template pierridotite/mobile-agent-testers --clone
cd my-testers && ./setup.sh           # par de claves + secrets + token de Claude (Windows: .\setup.ps1)
gh workflow run agent-testers.yml     # demo: 2 testers Android + 2 iOS, ~20 min
bash scripts/collect.sh <run id>      # descifra los informes y agrupa duplicados: runs/<id>/SUMMARY.md
```

La app de demo tiene [11 errores puestos a propósito](demo-app/BUGS.md). En la ejecución grabada de arriba, los 4 testers de la demo encontraron 9 (de 2 a 7 minutos por agente, unos 21 minutos en total con las compilaciones), además de problemas reales que nadie había puesto (un botón bajo la barra de navegación de Android, datos que no se guardan al reiniciar). Uso del modelo: 0,87 $ para los 4.

O deja que Claude lo configure para tu app:

```
/plugin marketplace add pierridotite/mobile-agent-testers
/plugin install mobile-agent-testers@mobile-agent-testers
```

## ¿Por qué no Maestro, Appium o agent-device?

Ejecutan las pruebas que tú escribes. Estos agentes buscan lo que nadie pensó en probar.

| | mobile-agent-testers | Maestro, Appium, Detox, e2e |
|---|---|---|
| Tú escribes | Nada: eliges personas de la lista | Flujos o código de prueba |
| Detecta | Diseño con texto grande, modo oscuro, textos confusos, callejones sin salida | Lo que comprueba cada prueba |
| Mismo resultado en cada ejecución | No: cada ejecución explora, así que revisa las capturas | Sí |

[agent-device](https://github.com/callstackincubator/agent-device) da a un agente de programación el control de un simulador. Esto ejecuta una sesión completa: compila la app, da a cada persona su propio dispositivo y recoge informes cifrados. Usa agentes antes de una versión y flujos con script para las regresiones.

Comparativa completa, con Firebase Test Lab Robo, mobile-mcp, phonedriver y beta testers humanos: [docs/compare.md](docs/compare.md) (en inglés).

## Prueba tu propia app

```bash
gh workflow run agent-testers.yml -f source_repo=you/app -f app_id=com.you.app \
  -f android_personas=anna,malik -f ios_personas=clara,jonas
```

| Entrada | |
|---|---|
| `source_repo`, `ref` | Repositorio y rama de la app (vacío = este repositorio). Repositorio privado: añade un secret `SOURCE_REPO_TOKEN` de solo lectura |
| `app_dir`, `app_id` | Carpeta de la app, paquete de Android / bundle id de iOS (si la otra plataforma usa otro id, se lee de su app compilada) |
| `android_personas`, `ios_personas` | Ids de [personas.json](personas.json), un teléfono cada una, `all`, o `none` para saltar una plataforma. 20 listas: 14 idiomas, derecha a izquierda, tabletas, texto desde pequeño hasta el mayor tamaño de accesibilidad |
| `brief` | Instrucciones para los agentes ([AGENT_BRIEF.md](AGENT_BRIEF.md)) |
| `framework` | `auto` (por defecto) o fuerza uno de los frameworks de abajo |
| `android_build` + `apk_path`, `ios_build` + `ios_app_path` | Tu propio comando de compilación, o la descarga de una app ya compilada (rutas relativas a `app_dir`) |
| `block_hosts` | Hosts de analítica bloqueados durante las pruebas |
| `record_video` | Grabación de pantalla de cada teléfono, cifrada con los informes |

**Compatibles de serie** (detección automática):

| Framework | Android | Simulador de iOS |
|---|---|---|
| Flutter | `flutter build apk --debug` | `flutter build ios --simulator` |
| React Native / Expo | Gradle release | Xcode, arm64 |
| Kotlin / Java, Swift / Objective-C nativos | Gradle debug | Xcode, arm64 |
| Kotlin Multiplatform | Gradle debug | Proyecto Xcode de la app de iOS |
| Capacitor / Ionic | Gradle debug tras `cap sync` | Xcode tras `cap sync` |
| .NET MAUI (beta) | `dotnet publish` | `dotnet build` para `iossimulator-arm64` |
| Cualquier otro | `android_build` + `apk_path` | `ios_build` + `ios_app_path` |

Los agentes leen la pantalla a partir de capturas y del árbol de accesibilidad, así que funciona con cualquier
toolkit de interfaz. Los widgets con etiqueta (`Semantics` de Flutter, `contentDescription`,
`accessibilityLabel`) les dan toques más precisos.

## Cómo funciona

<p align="center"><img src="assets/how-it-works.svg" alt="Cómo funciona: un workflow compila la app, luego un emulador o simulador con un agente por persona, informes cifrados, resumen en tu máquina" width="100%"></p>

- **Las personas** definen el dispositivo: modelo, sistema, tamaño de letra, modo oscuro, idioma, ubicación.
- **Tres herramientas por agente**: ver la pantalla (con coordenadas para tocar), gestos, escribir.
- **Revisión de accesibilidad** en cada pantalla: controles sin nombre y zonas táctiles por debajo de 48 dp (Android) o 44 pt (iOS), que el agente confirma en la captura.
- **Resultados cifrados**: los logs de un repositorio público son públicos, así que todo se cifra con tu clave.
- **Analítica bloqueada** dentro de los teléfonos, para que las pruebas nunca toquen tus estadísticas reales.
- **Un resumen** en tu máquina: Claude agrupa los informes que describen el mismo error, así ves cuántas personas encontraron cada uno y qué personas encontraron cada tipo de problema.
- **Pruebas** en cada push, sin conexión y sin teléfono: revisión de accesibilidad, matriz de personas, resumen, resultados cifrados ([tests/](tests/)).

## Límites

- Los runners de GitHub son gratis para repositorios públicos: unos 20 trabajos a la vez, 5 en macOS.
- En planes con un límite de uso de 5 horas, 20 agentes pueden agotarlo en ~15 min: ejecuta tandas de 6 a 10.
- Los runners alojados están pensados para el proyecto del propio repositorio. Para una app de código cerrado, ejecuta el workflow en tu repositorio privado o en tu propio Mac.

## Preguntas frecuentes

### ¿20 agentes no encuentran 20 veces el mismo error?

No. En LocalSend, los 103 informes eran 46 errores distintos, y 29 de ellos los encontró un solo agente, incluido el único bloqueante ([ver la ejecución](docs/runs/localsend-20.md)). Los errores de derecha a izquierda solo vinieron de las dos personas en árabe, y los de tableta de las cuatro tabletas. Los duplicados eran estados de toda la app con los que todos se cruzan, como la lista de dispositivos vacía.

### ¿Cuánto cuesta?

Los runners de GitHub son gratis para repositorios públicos, macOS incluido. El uso del modelo fue de 0,15 a 0,55 $ por agente en [estas ejecuciones](docs/runs/), unos 5 $ para 20 teléfonos. Con una suscripción a Claude, las ejecuciones cuentan en el uso de tu plan en lugar de facturarse.

### ¿Cuánto tarda una ejecución?

Cada agente explora de 1 a 18 minutos. Los 10 agentes Android de AnkiDroid tardaron menos de 10 minutos desde el inicio hasta el último informe. Los 20 dispositivos de LocalSend tardaron 69 minutos, compilaciones incluidas, porque el plan gratuito ejecuta 5 trabajos de macOS a la vez.

### ¿Necesito un Mac?

No. Todo se ejecuta en los runners de GitHub: Linux para Android, macOS para iOS. Necesitas la CLI `gh` y una suscripción a Claude o una clave de API, y `./setup.sh` (`.\setup.ps1` en Windows) hace el resto.

### ¿Dos ejecuciones dan el mismo resultado?

No. Cada agente explora, así que dos ejecuciones nunca siguen el mismo camino: espera los mismos tipos de errores, no la misma lista. Mantén las pruebas con script (Maestro, Appium) para las regresiones, mira [la comparativa](docs/compare.md).

### ¿Mis informes son públicos?

No. Los logs de un repositorio público son públicos, así que los informes, las capturas y los vídeos se cifran con tu clave antes de salir del runner, y solo tú puedes descifrarlos. Los hosts de analítica se bloquean dentro de los teléfonos. Usa cuentas de prueba, nunca reales. Más en [PRIVACY.md](PRIVACY.md).

### ¿Puedo probar una app de código cerrado?

Sí. Ejecuta el workflow desde un repositorio privado, con un `SOURCE_REPO_TOKEN` de solo lectura para el repositorio de tu app, o haz que `android_build` e `ios_build` descarguen un APK o un .app ya compilados. Los repositorios privados consumen tus minutos de Actions, y los minutos de macOS cuentan diez veces.

### ¿Puedo crear mis propias personas?

Sí. Una persona son unas pocas líneas en [personas.json](personas.json): dispositivo, versión del sistema, idioma, tamaño de texto, modo oscuro, ubicación, quién es y qué intenta hacer.

### ¿En qué se equivoca?

A veces interpreta mal una pantalla: 3 de los 20 agentes de LocalSend señalaron el teclado en inglés del simulador como parte de la app. Unos minutos por agente cubren los caminos principales, no cada rincón de una app grande. Cada hallazgo viene con capturas numeradas, así que revísalas antes de reportar nada.

## Historial de estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date)](https://star-history.com/#pierridotite/mobile-agent-testers&Date)

## Créditos

[Claude Code](https://docs.claude.com/en/docs/claude-code) ·
[AXe](https://github.com/cameroncooke/axe) ·
[android-emulator-runner](https://github.com/ReactiveCircus/android-emulator-runner)

Hecho por [@pierridotite](https://github.com/pierridotite) ([LinkedIn](https://www.linkedin.com/in/pierre-raffalli/)) · licencia MIT
