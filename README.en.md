🌐 [Castellano](README.md)

# GURO

**Conversion kit for Robobloq Qoopers robots with [BBC Micro:bit](https://www.microbit.org)**

Fundación Sadosky develops the GURO kit to upgrade Robobloq Qoopers robots — already deployed in schools across the country — by replacing the proprietary Qmind Plus controller with the [BBC Micro:bit](https://www.microbit.org): an educational board with fully open hardware and software, with an active global community of millions of teachers and students.

![GURO assembled](docs/user-guide/assets-GURO/GURO_final.png)

---

## What is the GURO kit?

The GURO kit consists of an **adapter board** (KiCad design included in this repository) and a **case** that allow mounting a BBC Micro:bit and a [Kittenbot Robotbit](https://kittenbothk-eng.readthedocs.io/en/latest/Microbit_eboard/Robotbit/robotbitMC.html) expansion board on the Robobloq Qoopers chassis, connecting the robot's existing motors and sensors.

The result is a functional robot, programmable from the browser using visual blocks or Python, without depending on any proprietary software or a single vendor.

The robot's 3D models and the case are available in this repository and on [Tinkercad](https://www.tinkercad.com/things/2tzfirybpMV-guro-microrbit-para-robolboq-qoopers-260401).

---

## Requirements

- **Robobloq Qoopers kit** — chassis, motors, sensors and mechanical parts (without the Qmind Plus)
- **GURO kit** — adapter board and Micro:bit case (this repository)
- **[BBC Micro:bit](https://www.microbit.org)** v1 or v2
- A Phillips screwdriver
- A computer with a USB port

---

## Assembly guide

The complete documentation is published at:

**[guro.readthedocs.io](https://guro.readthedocs.io/)**

It includes the parts inventory, 16 illustrated steps, and programming instructions. Also available [in PDF](docs/user-guide_2026-04-01.pdf).

---

## Programming the robot

Once the GURO is assembled, load a program onto the Micro:bit from the browser, without installing anything:

### Option 1 — Visual blocks (MakeCode)

Use the [Microsoft MakeCode](https://makecode.microbit.org) editor with the **Kittenbot Robotbit** extension to program the robot with blocks. [See the extension instructions.](https://kittenbothk-eng.readthedocs.io/en/latest/Microbit_eboard/Robotbit/robotbitMC.html)

### Option 2 — Python

Use the [official MicroPython editor](https://python.microbit.org/v/3) from the [Micro:bit Educational Foundation](https://github.com/microbit-foundation).

The [**microbitML**](https://github.com/fundacion-sadosky/microbitML) framework (Fundación Sadosky) includes the `mbGURO` activity, ready to command the robot. You can download the `.hex` file and flash it directly to the board.

---

## Repository structure

```
docs/               Site documentation (properDocs + Obsidian)
kit GURO/           Kit inventory
gabinete/           Case for the Micro:bit and expansion board
placa adaptadora/   Adapter PCB design (KiCad)
scripts/            Documentation generation scripts (properDocs/MkDocs)
mkdocs.yml          Documentation site configuration
docs-requirements.txt  Python dependencies to build the documentation
```

The `docs/` folder is configured as an [Obsidian](https://obsidian.md) vault, which allows editing it without using the terminal. See [Contributions for writers](https://guro.readthedocs.io/contributing/for-writers/).

---

## Collaboration opportunities

Here are some concrete tasks you can contribute to the project:

1. **Sightings**: if it's used in your school, share the experience B)
1. **Complete the Mechanics**: migrate the 3D case design from [Tinkercad](https://www.tinkercad.com/things/2tzfirybpMV-guro-microrbit-para-robolboq-qoopers-260401) to a maintainable/parametric format such as openScad.
1. **Complete the Mechanics**: the hood does not fit the case lid.
1. **Complete the Mechanics**: the case lid clashes with the Kittenbot battery holder.
1. **Complete the Guide**: steps 13, 14 and 16 of the assembly guide do not yet have images. If you have an assembled kit, you can take the photos and open a PR.
1. **Create a MakeCode extension specific to GURO**: the generic Kittenbot Robotbit extension is currently used. A dedicated extension would simplify block programming with names and functions tailored to the GURO.

## Contributing

Contributions are welcome, regardless of technical background.

- **Writers and teachers**: edit the documentation with [Obsidian](https://obsidian.md) by opening the `docs/` folder as a vault. See [guide for writers](https://guro.readthedocs.io/contributing/for-writers/).
- **Developers**: see the [guide for developers](https://guro.readthedocs.io/contributing/for-developers/).
- **Bugs or suggestions**: open an [issue](../../issues) in this repository.

---

## Credits

Initial contributors, in alphabetical order:

| Name | Role |
|---------------------------|-----------------------------|
| Alarcón Lasagno, Ramiro   | Doc, SW, HW                 |
| Batlle, Leandro           | Doc, SW, HW, original idea  |
| Gentile Montes, Ezequiel  | Mechanics                   |
| Medel, Ricardo            | Doc licenses, FLOSS, OSHW   |

*Did you contribute to the project? Open a PR to add your name and contributions.*

This project uses the [BBC Micro:bit](https://www.microbit.org), developed by the [Micro:bit Educational Foundation](https://github.com/microbit-foundation). The Micro:bit Foundation publishes its hardware specifications, firmware and educational resources under open licenses at [github.com/microbit-foundation](https://github.com/microbit-foundation).

---

## Trademarks

The product names and brands mentioned in this repository (including BBC Micro:bit, Robobloq, Qoopers, Kittenbot, Robotbit, Microsoft MakeCode, among others) are the property of their respective owners and are used solely for identification and descriptive purposes.

## Nature of the project

Development began at Fundación Sadosky within the framework of the Programa para el Desarrollo de la Infraestructura destinada a Promover la Capacidad Emprendedora funded by [CAF | Banco de desarrollo de América Latina y El Caribe](https://www.caf.com/). GURO is a conversion kit that allows reusing the mechanical parts, motors and sensors of the Robobloq Qoopers with a new controller board. The project does not modify or redistribute the firmware, software or hardware designs of the third-party products it integrates.

## Warranties and liability

This project is distributed without warranty of any kind, express or implied. Assembly, use and any modification of the kit are the sole responsibility of the user. Consult the GPLv3 and CC BY-SA 4.0 licenses included in this repository for the full terms. Use of the kit in educational settings must be carried out under teacher supervision and in accordance with the safety regulations applicable in each jurisdiction.

## Licenses

The project is distributed under a **dual license**:

### Code and hardware designs
Published under the [**GNU General Public License v3.0**](LICENSE) (GPLv3).
You may use, modify and redistribute the code and KiCad designs, provided that any derivative work is published under the same license.

### Documentation
Published under [**Creative Commons Attribution-ShareAlike 4.0 International**](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0).
You may copy, adapt and redistribute the content — even for commercial purposes — provided that you credit the original authors and distribute derivative works under the same license.

---

<p align="center">
  <a href="https://www.fundacionsadosky.org.ar">Fundación Sadosky</a>
</p>
