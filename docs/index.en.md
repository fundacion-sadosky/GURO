---
title: Home
---

# GURO

**Conversion kit for Robobloq Qoopers robots with [BBC Micro:bit](https://www.microbit.org)**

Fundación Sadosky develops the GURO kit to upgrade Robobloq Qoopers robots — already deployed in schools across the country — by replacing the proprietary Qmind Plus controller with the [BBC Micro:bit](https://www.microbit.org): an educational board with fully open hardware and software, with an active global community of millions of teachers and students.

![GURO assembled](assets-GURO/GURO_final.png)

---

## What is the GURO kit?

The GURO kit consists of an **adapter board** and a **case** that allow mounting a BBC Micro:bit and a [Kittenbot Robotbit](https://kittenbothk-eng.readthedocs.io/en/latest/Microbit_eboard/Robotbit/robotbitMC.html) expansion board on the Robobloq Qoopers chassis, connecting the robot's existing motors and sensors.

The result is a functional robot, programmable from the browser using visual blocks or Python, without depending on any proprietary software or a single vendor.

The kit designs and the 3D model of the case are available in the [project repository](https://github.com/fundacion-sadosky/GURO) and on [Tinkercad](https://www.tinkercad.com/things/2tzfirybpMV-guro-microrbit-para-robolboq-qoopers-260401).

---

## Quick access

| I want to… | Go to |
|---|---|
| Assemble the robot | [Getting started](getting-started.md) |
| Read the full assembly guide | [User guide](user-guide/index.md) |
| Contribute to the project | [Contributing](contributing/index.md) |
| View source code and designs | [github.com/fundacion-sadosky/GURO](https://github.com/fundacion-sadosky/GURO) |
| Download the adapter board (KiCad) | [placa adaptadora/](https://github.com/fundacion-sadosky/GURO/tree/main/placa%20adaptadora) |
| Download the case (STL) | [gabinete/](https://github.com/fundacion-sadosky/GURO/tree/main/gabinete) |
| Report a bug or suggest an improvement | [Issues](https://github.com/fundacion-sadosky/GURO/issues) |
| Guide in PDF | [user-guide_2026-04-01.pdf](https://github.com/fundacion-sadosky/GURO/raw/main/docs/user-guide_2026-04-01.pdf) |

---

## Requirements

- **Robobloq Qoopers kit** — chassis, motors, sensors and mechanical parts (without the Qmind Plus)
- **[GURO kit](https://github.com/fundacion-sadosky/GURO/tree/main/kit%20GURO)** — the official one or a handmade assembly
- **[BBC Micro:bit](https://www.microbit.org)** v1 or v2
- A Phillips screwdriver
- A computer with a USB port

---

## Programming the robot

Once the GURO is assembled, load a program onto the Micro:bit from the browser, without installing anything:

**Option 1 — Visual blocks:** use [Microsoft MakeCode](https://makecode.microbit.org) with the **Kittenbot Robotbit** extension.

**Option 2 — Python:** use the [official MicroPython editor](https://python.microbit.org/v/3). The [**microbitML**](https://github.com/fundacion-sadosky/microbitML) framework (Fundación Sadosky) includes the `mbGURO` activity, ready to command the robot.

---

## Repository

The entire project is open code and hardware:

- **Main repository:** [github.com/fundacion-sadosky/GURO](https://github.com/fundacion-sadosky/GURO)
- **Adapter board design (KiCad):** [placa adaptadora/](https://github.com/fundacion-sadosky/GURO/tree/main/placa%20adaptadora)
- **3D model of the case (STL):** [gabinete/](https://github.com/fundacion-sadosky/GURO/tree/main/gabinete)
- **Kit inventory:** [kit GURO/](https://github.com/fundacion-sadosky/GURO/tree/main/kit%20GURO)
- **Issues and suggestions:** [github.com/fundacion-sadosky/GURO/issues](https://github.com/fundacion-sadosky/GURO/issues)
- **Contributing:** [CONTRIBUTING.md](https://github.com/fundacion-sadosky/GURO/blob/main/CONTRIBUTING.md)
- **Code of conduct:** [CODE_OF_CONDUCT.md](https://github.com/fundacion-sadosky/GURO/blob/main/CODE_OF_CONDUCT.md)

The project is distributed under a dual license: **GPLv3** for code and hardware designs, **CC BY-SA 4.0** for documentation.

---

<p align="center">
  <a href="https://www.fundacionsadosky.org.ar">Fundación Sadosky</a>
</p>
