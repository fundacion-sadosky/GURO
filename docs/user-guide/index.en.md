---
title: User guide — GURO Assembly
nro:
---

# GURO — Assembly tutorial

This guide explains, step by step, how to assemble the **Standard** configuration of the **GURO kit**.

The goal is to transform the Robobloq Qoopers robot into a functional robot based on fully open designs.
We will use the [BBC Micro:bit](https://www.microbit.org) as the controller instead of the original Qmind Plus.

![GURO assembled](assets-GURO/GURO_final.png)

---

## Parts inventory

Before you begin, lay out all parts on a flat surface and check them against the list below.

![Parts list](assets-GURO/GURO_piezas.png)

| Part | Qty. | Part | Qty. |
| --- | --- | --- | --- |
| Qmind Plus board | 1 | Battery holder | 1 |
| Battery | 1 | LED panel | 1 |
| Motor | 2 | Wheel hub | 2 |
| Wheel | 2 | Light sensor | 1 |
| Ultrasonic sensor | 1 | Sound sensor | 1 |
| Gyroscope sensor | 1 | Track | 2 |
| 6-hole beam | 2 | 10-hole beam | 2 |
| 2-hole beam | 1 | Rectangular base | 1 |
| Triangular plate | 4 | Rectangular plate | 2 |
| Angular plate | 2 | Angular plate C | 2 |
| Arm plate | 2 | L-bracket | 2 |
| Large U-bracket | 1 | Small U-bracket | 1 |
| U-bracket | 1 | Ball bearing | 4 |
| Ball axle | 1 | Small plastic tube | 2 |
| Large plastic tube | 2 | Small bumper | 1 |
| Large bumper | 1 | Right mudguard | 1 |
| Left mudguard | 1 | Spoiler | 1 |
| Motor cable | 2 | RJ25 cable 150 mm | 2 |
| RJ25 cable 200 mm | 3 | Micro USB cable | 1 |
| USB cable | 1 | M4×9 mm screw | 35 |
| M4×15 mm screw | 30 | M4×20 mm screw | 10 |
| M4×30 mm screw | 10 | M4×42 mm screw | 10 |
| M3×8 mm screw | 5 | M4 nut | 60 |
| Lock nut | 5 | Screwdriver | 1 |
| Wrench | 1 | User manual | 1 |

> [!note] About the Qmind Plus board
> The Qmind Plus board is **not used** in the GURO kit: it is replaced by the **Micro:bit case**, assembled in Step 11. You may keep it for another project supported by the Robobloq company.

---

## Section 1 — Chassis and motors

### Step 1 — Assemble the chassis frame

**Parts needed:**
- 2 × 10-hole beams
- 1 × 6-hole beam
- 2 × M4×15 mm screws
![Parts for step 1](assets-GURO/GURO_1.png)

Join the two **10-hole beams** in parallel, connecting them at their ends with a **6-hole beam** using M4×15 mm screws. The result is a rectangular frame that forms the base of the chassis.
>[!tip] The holes of the long beams must line up as shown in the diagram

![Result of step 1](assets-GURO/GURO_1f.png)

---

### Step 2 — Mount the motors (presenting the parts)

**Parts needed:**
- 2 × motors
- 2 × wheel hubs
- 2 × triangular plates
- 4 × M4×15 mm screws and nuts
- 2 × M4×9 mm screws

![Parts for step 2](assets-GURO/GURO_2.png)
Place one **triangular plate** at each free end of a beam, as a bracket, and secure everything with two M4×15 mm screws and nuts (loosely).
Insert the two **motors** inside the rectangular frame, with the output shaft facing outward, and fix them with M4×9 mm screws. See the following detail:

The result is a chassis with the drive motors and main wheels mounted. The screws remain loose and the wheel hubs are not yet fixed. "Presenting the parts."

![Result of step 2](assets-GURO/GURO_2f.png)

---

### Step 3 — Mount the motors (tightening the parts)

**Parts needed:**
- 1 × rectangular plate
- 2 × M4×9 mm screws
- 2 × M3×8 mm screws

![Parts for step 3](assets-GURO/GURO_3.png)

Place the **rectangular plate** on the **bottom** face of the motors, aligning the mounting holes with those of the motors (**not** the chassis). Secure it with 2 M4×9 mm screws, tightly. This plate closes the base of the chassis and provides a mounting surface for internal components. Tighten the 6 screws on the triangular plates (from the previous step — if necessary, temporarily remove the wheel hubs). Fix the wheel hubs with M3×8 mm screws.

![Result of step 3](assets-GURO/GURO_3f.png)

---

### Step 4 — Complete the chassis frame

**Parts needed:**
- 1 × U-plate ("U-bracket")
- 4 × M4×15 mm screws and nuts

![Parts for step 4](assets-GURO/GURO_4.png)

Attach the **U-plate** to the chassis, skipping the first hole of each beam, and fixing the plate at the second and third hole of the beam.
The result is the complete lower chassis, robust and ready to receive the running gear.

![Result of step 4](assets-GURO/GURO_4f.png)

---

## Section 2 — Wheels, mudguards and tracks

### Step 5 — Mount the non-drive wheels

**Parts needed:**
- 2 × wheel hubs
- 4 × ball bearings
- 2 × short plastic tubes
- 2 × long plastic tubes (16 mm)
- 2 × M4×42 mm screws
- 2 × M4 lock nuts

![Parts and detail for step 5](assets-GURO/GURO_5.png)

Prepare the two remaining wheel hubs as follows: insert two bearings (one on each side) with a small tube in between. The wheel hub looks the same; the bearings do not protrude.

Insert an M4×42 mm screw (the axle) from the inner side of the chassis and a **long plastic tube** from the outer side. Insert the wheel (bearing + hub + spacer + bearing assembly) onto the axle and secure with a **lock nut** (not a standard one). Repeat for the opposite side. These non-drive wheels must spin freely and will guide the tracks.

>[!tip] You can get ahead and do step 10, fitting the tracks to test the tension between the wheels. Stretch each **track** over the complete set of wheels on one side — drive wheel and non-drive wheels — simultaneously, distributing the band evenly around all wheels. Do not force one section at a time. Repeat for the opposite side. Check that the tracks move with minimal effort.

---

### Step 6 — Attach the mudguards

**Parts needed:**
- 2 × mudguards
- 4 × M4×9 mm screws and nuts

![Parts for step 6](assets-GURO/GURO_6.png)

Place each **mudguard** on the side of the chassis, at the end of the long beam, over the motor. Secure each one with 2 M4×15 mm screws. Repeat on the other side.
The mudguards protect the GURO from accidental impacts and allow sensors such as the accelerometer, microphone, etc. to be mounted.

![Result of step 6](assets-GURO/GURO_6f.png)

---

## Section 3 — Body

### Step 7 — Mount the top platform

**Parts needed:**
- 1 × rectangular base
- M4×15 mm screws

![Parts for step 7](assets-GURO/GURO_7.png)

Place the **rectangular base** on the side beams of the chassis, aligning its holes with those of the beams, but shifted forward by two rows. Fix it with M4×15 mm screws. Nuts are not required because the **rectangular base** has threaded holes.

![Result of step 7](assets-GURO/GURO_7f.png)
This platform is the surface on which all electronic components are mounted, and it is also used to secure the battery underneath (in step 15, which is why it is shifted two rows forward from the chassis).

---

### Step 8 — Install the Micro:bit protection

**Parts needed:**
- 1 × large U-bracket
- 2 × "angular C" plates
- 4 × M4×9 mm screws and nuts

![Parts for step 8](assets-GURO/GURO_8.png)

Screw one **"angular C" plate** to each side of the **large U-bracket** with M4×9 mm screws and nuts, leaving them loose.
Before screwing the "angular C" plates to the chassis, take two M4×9 mm screws and thread a nut onto each until there is no gap between the nut and the head.
Those nut + screw assemblies will be the pivot of the "angular C" plates — screw them firmly against the chassis (the short beam below the rectangular plate).
Slide the **U-bracket** against the chassis (as in the final figure) and tighten the 4 screws firmly.

The hood protects the Micro:bit case from accidental impacts and can be lifted to access the electronics.

![Result of step 8](assets-GURO/GURO_8f.png)

---

### Step 9 — Assemble and mount the LED panel bracket

**Parts needed:**
- 1 × LED panel
- 1 × "L-bracket"
- 1 × spoiler
- 3 × M4×15 mm screws and nuts
- 2 × M4×42 mm screws and nuts

![Parts for step 9](assets-GURO/GURO_9.png)
![Parts for step 9](assets-GURO/GURO_9b.png)
Join the **spoiler** to the **LED panel** with one M4×15 mm screw on each side. Note the corresponding hole on the panel (shown in grey in the diagram).

The LED panel will be joined to the chassis via the "L-bracket": one M4×42 mm screw with a lock nut on the side of

![Detail: ball bearing insertion](assets-GURO/GURO_9c.png)
![Detail: ball bearing insertion](assets-GURO/GURO_9a.png)

Secure the complete support at the front of the chassis using the **L-bracket** with one M4×9 mm screw. The LED panel faces forward at a slightly angled position.

![Result of step 9](assets-GURO/GURO_9f.png)

> [!tip] LED panel orientation
> The face with the LEDs must be pointing toward the front of the robot. Verify this before tightening the screws definitively.

---

### Step 10 — Attach the tracks

**Parts needed:**
- 2 × tracks (rubber bands)

![Parts for step 10](assets-GURO/GURO_10.png)

Stretch each **track** over the complete set of wheels on one side — drive wheel and idler wheels — simultaneously, distributing the band evenly around all wheels. Do not force one section at a time. Repeat for the opposite side.

![Result of step 10](assets-GURO/GURO_10f.png)

> [!tip] Tension check
> Turn each drive wheel by hand. The track should move smoothly, without jumps or folds.

---

## Section 4 — Electronics

### Step 11 — Assemble the Micro:bit case

**Parts needed:**
- 1 × case base board
- 1 × expansion board (carrier board)
- 1 × BBC Micro:bit
- 1 × case lid (grey bracket)
- 4 × M3×8 mm screws

![Parts for step 11](assets-GURO/GURO_11.png)

Place the **expansion board** on the **base board** and fix it with M3×8 mm screws. Connect the **Micro:bit** to the expansion board by carefully inserting the edge connector (the side with the gold pins) into the corresponding slot. Finally, snap the **lid** onto the assembly to protect the top connections.

![Assembly detail](assets-GURO/GURO_11a.png)

The result is the complete **Micro:bit case**: the brain of the GURO, ready to be mounted on the robot.

![Result of step 11](assets-GURO/GURO_11f.png)

> [!note] The Micro:bit replaces the Qmind Plus
> The [BBC Micro:bit](https://www.microbit.org) is a microcontroller with fully open code and hardware, with an active community of millions of users worldwide. It is programmed for free from the browser — without installing any software — using visual blocks or Python. Unlike the Qmind Plus, its specifications are public, its firmware is auditable, and it does not depend on a single vendor for continuity.

---

### Step 12 — Mount the Micro:bit case on the robot

**Parts needed:**
- 1 × Micro:bit case (assembled in the previous step)
- 2 × M4×9 mm screws
- 2 × M4 nuts

![Parts for step 12](assets-GURO/GURO_12.png)

With the hood raised, place the **Micro:bit case** on the top platform of the chassis, aligning the holes of the base board with those of the platform. Fix it with 2 M4×9 mm screws and M4 nuts.

![Detail: positioning](assets-GURO/GURO_12a.png)

Close the hood. The Micro:bit LED display must be visible through the front opening.

![Result of step 12](assets-GURO/GURO_12f.png)

---

## Section 5 — Wiring and battery

### Step 13 — Connect the motors

> [!warning] Images pending
> Photographs for this step will be published soon.

Connect the **motor cable** of each motor to the corresponding port on the expansion board in the Micro:bit case. The connectors are 2-pin and have a single insertion direction. Each motor has its designated port: left and right.

---

### Step 14 — Connect the sensors

> [!warning] Images pending
> Photographs for this step will be published soon.

Connect each sensor (ultrasonic, light, sound, gyroscope) to its corresponding RJ25 port on the expansion board using the **RJ25 cables**. Use the 150 mm cables for the front sensors and the 200 mm cables for the side or rear sensors.

---

### Step 15 — Install the battery holder and front bumper

**Parts needed:**
- 1 × **battery holder** (without battery)
- 2 × M4×42 mm screws and *lock nuts*
- 1 × large bumper

![Parts for step 15](assets-GURO/GURO_15.png)

Slide the **battery holder** under the chassis, on the side of the non-drive wheels, with the gap facing forward. Secure the holder and the **large bumper** with two M4×42 mm screws and **lock nuts** to the first row of the **rectangular base** installed in step 7.

![Result of step 15](assets-GURO/GURO_15f.png)

---

### Step 16 — Connect the LED panel

> [!warning] Images pending
> Photographs for this step will be published soon.

Connect a **150 mm RJ25 cable** to the rear port of the **LED panel**. Route the cable through the inside of the holder and connect the other end to the designated RJ25 port on the expansion board.

---

## Assembly complete and control software

The GURO is ready. Connect the robot to your computer using the **Micro USB cable** and follow the programming guide to load your first program.

![GURO assembled](assets-GURO/GURO_final.png)

All done!! Or almost done...

The last touch that brings the GURO robot to life will be loading a program onto the micro:bit. Programming is outside the scope of this document, but there are two convenient options:

1. Program the Micro:bit with blocks in the [MS MakeCode](https://makecode.microbit.org) editor with the [Kittenbot Robotbit](https://kittenbothk-eng.readthedocs.io/en/latest/Microbit_eboard/Robotbit/robotbitMC.html) extension.
2. Program the Micro:bit with real Python using [the official editor](https://python.microbit.org/v/3). The [microbitML framework](https://github.com/fundacion-sadosky/microbitML) includes the `mbGURO` activity ready to command the GURO robot. You can download the .HEX file and upload it to the editor (or flash it directly to the board!).
