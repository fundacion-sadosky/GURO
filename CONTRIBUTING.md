# Guía de contribución

Las contribuciones al proyecto GURO son bienvenidas, independientemente de tu perfil técnico: docentes, diseñadores, desarrolladores y cualquier persona interesada puede participar.

Al contribuir, aceptás nuestro [Código de Conducta](CODE_OF_CONDUCT.md). Su lectura es un requisito previo a cualquier participación.

---

## Alcance del proyecto — qué se acepta y qué no

El kit GURO integra componentes propios (placa adaptadora, gabinete, documentación) junto con productos de terceros (BBC Micro:bit, Kittenbot Robotbit, Robobloq Qoopers). Este repositorio solo contiene los componentes propios del proyecto.

| Componente | ¿Modificable en este repo? | Licencia |
|---|---|---|
| Placa adaptadora GURO (KiCad) | Sí | GPLv3 |
| Gabinete GURO | Sí | GPLv3 |
| Documentación (`docs/`) | Sí | CC BY-SA 4.0 |
| Scripts (`scripts/`) | Sí | GPLv3 |
| Partes mecánicas, motores, sensores Robobloq | **No** | Propiedad de Robobloq Co., Ltd. |
| Firmware / software BBC Micro:bit | **No** | Licencias de Micro:bit Educational Foundation |
| Extensión Robotbit (MakeCode) | **No** | Licencia de Kittenbot |

### Se aceptan contribuciones que:

- Mejoren la placa adaptadora o el gabinete (diseños KiCad, archivos 3D mantenibles como openScad).
- Completen o corrijan la documentación (guía de armado, guías de contribución, traducciones).
- Agreguen o mejoren scripts de generación de documentación.
- Incluyan ejemplos de programación originales compatibles con las licencias del proyecto.
- Reporten errores, hagan preguntas o sugieran mejoras mediante issues.

### No se aceptan contribuciones que:

- Modifiquen, incluyan o redistribuyan firmware, software o diseños de hardware de productos de terceros (Robobloq, Kittenbot, Micro:bit Educational Foundation, u otros).
- Incluyan binarios precompilados de terceros, incluyendo archivos `.hex` que no sean producidos por este proyecto.
- Incluyan assets (imágenes, textos, código) con derechos de autor de terceros sin verificar compatibilidad de licencia con GPLv3 o CC BY-SA 4.0, según corresponda.
- Incluyan datos personales de cualquier persona, en particular de menores de edad (ver [Privacidad y protección de menores](#privacidad-y-protección-de-menores)).

Si querés modificar componentes de terceros (firmware de la Micro:bit, la extensión de Kittenbot, las piezas del Qoopers), el lugar correcto es el repositorio de cada fabricante, bajo sus propias licencias.

---

## Cómo contribuir

### Docentes y redactores

La documentación vive en la carpeta `docs/`, configurada como un vault de [Obsidian](https://obsidian.md). Podés editarla directamente desde la aplicación Obsidian, sin necesidad de usar la terminal ni conocer git.

Consultá la [guía para redactores](https://guro-tutorial.readthedocs.io/contributing/for-writers/) para más detalles sobre el flujo de edición y las convenciones del sitio.

Si encontrás un error o querés sugerir una mejora pero no querés editar directamente, abrí un [issue](../../issues) describiendo el problema.

### Desarrolladores

Consultá la [guía para desarrolladores](https://guro-tutorial.readthedocs.io/contributing/for-developers/) para detalles sobre el entorno, las herramientas utilizadas y las convenciones del proyecto.

El flujo de trabajo estándar es:

1. Hacé un fork del repositorio.
2. Creá una rama con un nombre descriptivo (`fix/paso-13-imagen`, `feat/traduccion-ingles`, etc.).
3. Realizá tus cambios y commiteá con mensajes claros.
4. Abrí un Pull Request hacia `main` describiendo qué cambia y por qué.

Los PRs deben pasar las verificaciones automáticas del repositorio antes de ser revisados.

### Cualquier persona

Podés abrir un [issue](../../issues) para:

- Reportar un error en la documentación o en los diseños.
- Sugerir una mejora o nueva funcionalidad.
- Hacer preguntas sobre el proyecto.
- Compartir tu experiencia usando el kit en el aula.

---

## Licencia de las contribuciones

Al enviar un Pull Request a este repositorio, declarás que:

- Tu contribución es tu trabajo original, o tenés derecho a enviarla bajo las licencias del proyecto.
- Publicás tu contribución bajo las licencias del repositorio: **GPLv3** para código y diseños de hardware, **CC BY-SA 4.0** para documentación.
- Entendés que tu contribución será pública y que otros podrán usarla según los términos de dichas licencias.

---

## Respeto a licencias de terceros

- No incluyas código, firmware ni assets de terceros sin verificar compatibilidad de licencia con GPLv3 o CC BY-SA 4.0, según el tipo de componente.
- Si tu contribución tiene una dependencia externa, documentá la dependencia y su licencia; no copies el componente al repositorio.
- El copyright de los contenidos creados en los servicios de la Micro:bit Educational Foundation pertenece a quien los creó. Si quien los creó es un menor, el copyright pertenece a ese menor. Tené esto en cuenta al incluir ejemplos de programación.

---

## Privacidad y protección de menores

El kit GURO se usa en escuelas, por lo que el proyecto interactúa directamente con docentes y, a través de ellos, con estudiantes que pueden ser menores de edad.

- No incluyas información personal identificable (nombres, instituciones, localidades, fotografías reconocibles) en ningún archivo del repositorio: código, documentación, ejemplos, imágenes ni comentarios de commits o issues.
- No incluyas imágenes ni videos de menores sin autorización expresa de sus tutores.
- Si contribuís con ejemplos creados por tus estudiantes, asegurate de que no contengan datos personales y de contar con las autorizaciones necesarias según la normativa aplicable en tu jurisdicción.
- Todos los espacios del proyecto (issues, PRs, discusiones, eventos presenciales) deben ser espacios seguros cualquier usuario o usuaria, especialmente si son menores.

Para referencia, consultá la [Safeguarding Policy de la Micro:bit Educational Foundation](https://microbit.org/safeguarding/).

---

## Créditos

Si tu contribución es incorporada al proyecto, podés agregar tu nombre a la tabla de créditos del `README.md`. El formato es:

```
| Apellido, Nombre | Rol |
```

Los roles pueden combinarse: `Doc` (documentación), `SW` (software), `HW` (hardware), `Mecánica`, `Traducción`, u otros descriptivos.

Abrí un PR que incluya únicamente el agregado de tu entrada en la tabla.
