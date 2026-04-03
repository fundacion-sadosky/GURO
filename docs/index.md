---
title: Inicio
---

# GURO

**Kit de conversión para robots Robobloq Qoopers con [BBC Micro:bit](https://www.microbit.org)**

La Fundación Sadosky desarrolla el kit GURO para actualizar los robots Robobloq Qoopers —ya desplegados en escuelas de todo el país— reemplazando el controlador propietario Qmind Plus por la [BBC Micro:bit](https://www.microbit.org): una placa didáctica de hardware y software completamente abiertos, con una comunidad global activa de millones de docentes y estudiantes.

![GURO terminado](assets-GURO/GURO_final.png)

---

## ¿Qué es el kit GURO?

El kit GURO consiste en una **placa adaptadora** y un **gabinete** que permiten montar una BBC Micro:bit y una placa expansora [Kittenbot Robotbit](https://kittenbothk-eng.readthedocs.io/en/latest/Microbit_eboard/Robotbit/robotbitMC.html) en el chasis del Robobloq Qoopers, conectando los motores y sensores existentes del robot.

El resultado es un robot funcional, programable desde el navegador en bloques visuales o en Python, sin depender de ningún software propietario ni de un único proveedor.

Los diseños del kit y el modelo 3D del gabinete están disponibles en el [repositorio del proyecto](https://github.com/fundacion-sadosky/GURO) y en [Tinkercad](https://www.tinkercad.com/things/2tzfirybpMV-guro-microrbit-para-robolboq-qoopers-260401).

---

## Accesos rápidos

| Quiero... | Ir a |
|---|---|
| Armar el robot | [Primeros pasos](getting-started.md) |
| Leer la guía completa de armado | [Guía de usuario](user-guide/index.md) |
| Contribuir al proyecto | [Contribuciones](contributing/index.md) |
| Ver el código fuente y los diseños | [github.com/fundacion-sadosky/GURO](https://github.com/fundacion-sadosky/GURO) |
| Descargar la placa adaptadora (KiCad) | [placa adaptadora/](https://github.com/fundacion-sadosky/GURO/tree/main/placa%20adaptadora) |
| Descargar el gabinete (STL) | [gabinete/](https://github.com/fundacion-sadosky/GURO/tree/main/gabinete) |
| Reportar un error o sugerir una mejora | [Issues](https://github.com/fundacion-sadosky/GURO/issues) |
| Guía en PDF | [user-guide_2026-04-01.pdf](https://github.com/fundacion-sadosky/GURO/raw/main/docs/user-guide_2026-04-01.pdf) |

---

## Requisitos

- **Kit Robobloq Qoopers** — chasis, motores, sensores y partes mecánicas (sin el Qmind Plus)
- **[Kit GURO](https://github.com/fundacion-sadosky/GURO/tree/main/kit%20GURO)** — el oficial o un armado artesanalmente 
- **[BBC Micro:bit](https://www.microbit.org)** v1 o v2
- Un destornillador Phillips
- Una computadora con puerto USB

---

## Programación del robot

Una vez armado el GURO, cargá un programa a la Micro:bit desde el navegador, sin instalar nada:

**Opción 1 — Bloques visuales:** usá [Microsoft MakeCode](https://makecode.microbit.org) con la extensión **Kittenbot Robotbit**.

**Opción 2 — Python:** usá el [editor oficial de MicroPython](https://python.microbit.org/v/3). El framework [**microbitML**](https://github.com/fundacion-sadosky/microbitML) (Fundación Sadosky) incluye la actividad `mbGURO`, lista para comandar al robot.

---

## Repositorio

Todo el proyecto es de código y hardware abiertos:

- **Repositorio principal:** [github.com/fundacion-sadosky/GURO](https://github.com/fundacion-sadosky/GURO)
- **Diseño de la placa adaptadora (KiCad):** [placa adaptadora/](https://github.com/fundacion-sadosky/GURO/tree/main/placa%20adaptadora)
- **Modelo 3D del gabinete (STL):** [gabinete/](https://github.com/fundacion-sadosky/GURO/tree/main/gabinete)
- **Inventario del kit:** [kit GURO/](https://github.com/fundacion-sadosky/GURO/tree/main/kit%20GURO)
- **Issues y sugerencias:** [github.com/fundacion-sadosky/GURO/issues](https://github.com/fundacion-sadosky/GURO/issues)
- **Contribuciones:** [CONTRIBUTING.md](https://github.com/fundacion-sadosky/GURO/blob/main/CONTRIBUTING.md)
- **Código de conducta:** [CODE_OF_CONDUCT.md](https://github.com/fundacion-sadosky/GURO/blob/main/CODE_OF_CONDUCT.md)

El proyecto se distribuye bajo licencia dual: **GPLv3** para código y diseños de hardware, **CC BY-SA 4.0** para documentación.

---

<p align="center">
  <a href="https://www.fundacionsadosky.org.ar">Fundación Sadosky</a> &nbsp;·&nbsp;
  <a href="https://program.ar">Iniciativa program.ar</a> &nbsp;·&nbsp;
  <a href="https://www.microbit.org">micro:bit</a>
</p>
