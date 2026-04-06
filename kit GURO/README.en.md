🌐 [Castellano](README.md)

# GURO Kit

The GURO kit is the set of parts and documents that allow converting a Robobloq Qoopers robot into a robot with fully open hardware and software, replacing the proprietary Qmind Plus controller with a BBC Micro:bit.

The manufacturing files for all kit parts are available in this repository: the adapter board design in the `placa adaptadora/` folder (KiCad) and the case model in the `gabinete/` folder (STL for 3D printing).

---

## Kit inventory

| Part                     | Qty. | Notes                                                  |
|--------------------------|---|--------------------------------------------------------|
| case (base)              | 1 | 3D printed. STL file in `gabinete/`                    |
| case (lid)               | 1 | 3D printed. STL file in `gabinete/`                    |
| Adapter board            | 1 | PCB designed in KiCad. Files in `placa adaptadora/`    |
| Kittenbot Robotbit board | 1 | Commercial PCB for Micro:bit expansion                 |
| Power board              | 1 | Commercial PCB that regulates voltage from the battery |
| Power cable              | 1 | Connects the battery to the power board                |


You can build your own kit ("DIY" or "maker") anywhere in the world from this repo's documentation:
1. For the adapter board, there are two options:
   2. Manufacture the PCB from the repo design
   3. Start from a prototype (or "universal") 50×70 mm board and solder the tracks and connectors
2. Print the case (base and lid)
2. Obtain the commercial components: Kittenbot Robotbit and the Power Board

---

## Required components (not included in the kit)

The GURO kit must be combined with the following components, obtained separately:

| Component | Notes |
|---|---|
| BBC Micro:bit v1 or v2 | Main controller board |
| Robobloq Qoopers kit | Does not need to be complete — see the assembly guide |

---

## Assembly guide

The complete step-by-step assembly guide is in the `docs/` folder and accessible at:

**[guro.readthedocs.io](https://guro.readthedocs.io/)**

Also available in PDF at `docs/user-guide_2026-04-01.pdf`.
