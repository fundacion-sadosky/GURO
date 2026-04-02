---
title: Contribuciones de documentación (para redactores)
---

# Contribuciones de documentación

No es necesario ser programador/a para contribuir a la documentación de este proyecto.
Solo necesitás [Obsidian](https://obsidian.md) (gratuito) y una cuenta de GitHub.

## Configuración inicial (~5 minutos)

1. **Forkeá** este repositorio en GitHub
2. **Cloná** el repositorio en tu computadora
3. Abrí la carpeta `docs/` como un **vault de Obsidian**
   (`Archivo → Abrir vault → Abrir carpeta como vault → seleccioná docs/`)
4. En Obsidian, accedé a `Configuración → Archivos y enlaces`:
    - Establecé **Ubicación predeterminada para nuevas notas** → `Misma carpeta que el archivo actual`
    - **Desactivá** `Usar [[Wikilinks]]` → usá enlaces Markdown estándar
    - Establecé **Formato de nuevos enlaces** → `Ruta relativa al archivo`

> [!tip] ¿Por qué desactivar los wikilinks?
> Los enlaces Markdown estándar (`[texto](archivo.md)`) funcionan en todos lados:
> en Obsidian, en GitHub y en el sitio de documentación.
> Los wikilinks (`[[archivo]]`) solo funcionan en Obsidian.

## Convenciones de escritura

### Lo que podés usar libremente

Estas funciones se comportan de la misma manera en Obsidian y en el sitio publicado:

- **Encabezados** (`# H1` hasta `#### H4`)
- **Negrita**, *cursiva*, ~~tachado~~, ==resaltado==
- Enlaces Markdown estándar: `[texto del enlace](otra-página.md)`
- Imágenes: `![texto alternativo](assets/imagen.png)`
- Bloques de código con resaltado de sintaxis
- Tablas
- Listas de tareas (`- [ ] pendiente`)
- Diagramas Mermaid (dentro de bloques ` ```mermaid `)
- Matemática LaTeX: `$en línea$` y `$$en bloque$$`
- Llamadas / admoniciones:

```text
> [!note] Título aquí
> Texto del cuerpo aquí.
>
> Admite **formato** y `código`.
```

Tipos de llamadas disponibles: `note`, `tip`, `warning`, `danger`, `example`,
`question`, `quote`, `info`, `bug`, `success`, `failure`, `abstract`.

### Qué evitar

| Función | Por qué | Alternativa |
|---|---|---|
| `[[wikilinks]]` | No es portable | `[texto](archivo.md)` |
| `![[embed]]` | No es portable | Copiá el texto relevante o enlazalo |
| `^referencias-de-bloque` | No son portables | Usá enlaces a encabezados: `[texto](archivo.md#encabezado)` |
| Plugins exclusivos de Obsidian | No se renderizan en el sitio | Usá Markdown estándar |

## Cómo enviar tus cambios

1. Creá una nueva **rama** para tus cambios
2. Escribí o editá los archivos `.md` dentro de `docs/`
3. **Commiteá** y **pusheá** a tu fork
4. Abrí un **Pull Request** en GitHub
5. La documentación se compilará y previsualizará automáticamente

> [!tip] Previsualizá antes de enviar
> Podés ver exactamente cómo va a quedar la documentación en el sitio.
> Pedile ayuda a un desarrollador para correr `mkdocs serve` localmente,
> o revisá la previsualización del PR en ReadTheDocs.
