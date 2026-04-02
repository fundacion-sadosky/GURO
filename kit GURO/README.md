# Kit GURO

El kit GURO es el conjunto de piezas y documentos, que permiten convertir un robot Robobloq Qoopers en un robot de hardware y software completamente abiertos, reemplazando el controlador propietario Qmind Plus por una BBC Micro:bit.

Los archivos de fabricación de todas las piezas del kit están disponibles en este repositorio: el diseño de la placa adaptadora en la carpeta `placa adaptadora/` (KiCad) y el modelo del gabinete en la carpeta `gabinete/` (STL para impresión 3D).

---

## Inventario del kit

| Pieza                    | Cant. | Notas                                                  |
|--------------------------|---|--------------------------------------------------------|
| gabinete (base)          | 1 | Impresa en 3D. Archivo STL en `gabinete/`              |
| gabinete (tapa)         | 1 | Impresa en 3D. Archivo STL en `gabinete/`              |
| Placa adaptadora         | 1 | PCB diseñada en KiCad. Archivos en `placa adaptadora/` |
| Placa Kittenbot Robotbit | 1 | PCB comercial para expansión de la micro:bit           |                      |
| Placa de alimentación    | 1 | PCB comercial que regula la tensión desde la batería   |            |
| Cable de alimentación    | 1 | conecta la batería con la placa de alimentación        |


Es posible armar tu propio kit ("DIY" o "maker") en cualquier lugar del mundo, a partir de la documentación de este repo:
1. para la placa adaptadora, hay dos opciones:
   2. fabricar el PCB con el diseño del repo
   3. partir de una placa de prototipado (o "universal") de 50x70 mm, y soldar las pistas y conectores
2. imprimiendo el gabinete (base y tapa)
2. consiguendo los componentes comerciales: Kittenbot Robotbit y Placa de Alimentación

---

## Componentes necesarios (no incluidos en el kit)

El kit GURO debe combinarse con los siguientes componentes, que se consiguen por separado:

| Componente | Notas                                     |
|---|-------------------------------------------|
| BBC Micro:bit v1 o v2 | Placa controladora principal              |
| Kit Robobloq Qoopers | no es necesario que esté completo, ver la Guía de armado|

---

## Guía de armado

La guía completa de armado paso-a-paso está en la carpeta `docs/` y accesible en:

**[guro.readthedocs.io](https://guro.readthedocs.io/)**

También disponible en PDF en `docs/user-guide_2026-04-01.pdf`.
