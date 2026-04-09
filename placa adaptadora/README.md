🌐 [English](README.en.md)

# Placa Adaptadora — Kit GURO

Diseño [KiCad](https://www.kicad.org/) de la **placa adaptadora**, componente del [kit GURO](../kit%20GURO/README.md).

---

## ¿Qué hace esta placa?

La placa adaptadora es el puente eléctrico central del kit GURO.
Conecta todos los periféricos del chasis Qoopers a la [Kittenbot Robotbit](https://kittenbothk-eng.readthedocs.io/en/latest/Microbit_eboard/Robotbit/robotbitMC.html):

```
Kittenbot Robotbit
      │
      ├── Motores (×2) — conectores de 6 pines
      ├── Sensores  ─┐
      ├── GPIO       ├── conectores RJ25 (6 Posiciones / 6 Contactos)
      └── Panel LED ─┘
```

También incorpora la conexión a la **placa de alimentación** del kit, PRECAUCIÓN:

> [!WARNING]
> NUNCA conectar la batería del Robobloq Qoopers directamente al Kittenbot Robotbit: es necesario regular su tensión a 5V (con 15W), que es la función de la "placa de alimentación".

---

## Vista del diseño PCB

![Diseño KiCad de la placa adaptadora](README.d/32ab5229be86394e9114bad1ba3fc2b0_MD5.jpg)

El diseño está optimizado para ser **intercambiable con una [placa universal de 50×70 mm](https://www.printables.com/model/797008-perfboard-50x70mm-18-x-24-holes)**, lo que permite replicarla sin acceso a fabricación de PCB profesional.

---

## Opciones de fabricación o reemplazo

| Opción | Dificultad | Resultado |
|--------|-----------|-----------|
| **A** — Fabricar con los archivos KiCad | Media — requiere enviar Gerbers a un fabricante | PCB profesional, reproducible |
| **B** — Placa universal 50×70 mm | Media — requiere soldadura | Resultado equivalente, sin fabricante externo |
| **C** — Conexión directa sin PCB | Baja — cables y dupont | Funcional, menos prolijo |

Cualquiera sea la opción elegida, el resultado eléctrico es equivalente.

---

## Opción A — Fabricar con los archivos KiCad

Los archivos de esta carpeta son un proyecto de [KiCad](https://www.kicad.org/) (software libre de diseño de PCB).

**Para fabricar:**
1. Abrí el proyecto en KiCad y exportá los **archivos Gerber** (Archivo → Fabricar → Gerbers)
2. Subí los Gerbers a cualquier servicio de fabricación de PCB (JLCPCB, PCBWay, Aisler, etc.)
3. Pedido típico: 5 unidades, 2 capas, FR4, 1.6 mm de espesor

**Para editar el diseño**, necesitás [KiCad 7 o superior](https://www.kicad.org/download/).

---

## Opción B — Placa universal 50×70 mm

### Componentes necesarios para soldar

| Componente | Cantidad | Notas |
|---|---|---|
| Placa universal perforada 50×70 mm | 1 | Paso de 2.54 mm |
| Conector RJ25 hembra (6P6C) | 5 | Para sensores y panel LED |
| Conector 2 pines macho (paso 2.54 mm) | 2 | Para motores |
| Pin header hembra 40 pines (paso 2.54 mm) | 2 | Para Kittenbot Robotbit |
| Cable de conexión (wire wrap o similar) | — | Para puentes entre pads |

### Procedimiento general

1. Posicioná los conectores RJ25 siguiendo el layout del PCB como referencia
2. Soldá los conectores y trazá los puentes según el esquemático KiCad
3. Verificá continuidad con multímetro antes de conectar

---

## Opción C — Conexión directa sin PCB

Si no disponés de soldador ni fabricante, es posible conectar directamente los periféricos a la Kittenbot Robotbit con **cables dupont**, sin PCB intermedio.

Consultá el [paso 13 (motores)](../docs/user-guide/index.md) y el [paso 14 (sensores)](../docs/user-guide/index.md) de la guía de armado para el detalle de cada conexión.

---

## Precauciones y Licencia

Aplican todas las licencias y precauciones de seguridad y salud citadas en el [apartado legal del repositorio principal](../README.md#garantías-y-responsabilidad), especialmente al realizar soldadura y manipulación de herramientas eléctricas.
