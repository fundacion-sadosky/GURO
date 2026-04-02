---
title: Contribuciones (para desarrolladores)
---

# Contribuciones (para desarrolladores)

## Stack de documentación

| Componente | Propósito |
|---|---|
| [MkDocs](https://www.mkdocs.org/) | Generador de sitios estáticos |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Tema visual |
| [mkdocstrings](https://mkdocstrings.github.io/) | Documentación de API automática desde docstrings |
| [mkdocs-obsidian-bridge](https://github.com/GooRoo/mkdocs-obsidian-bridge) | Soporte de wikilinks de Obsidian (fallback) |
| [mkdocs-gen-files](https://github.com/oprypin/mkdocs-gen-files) | Generación automática de páginas de referencia |

## Desarrollo local

```bash
# Crear un entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instalar dependencias de documentación
pip install -r docs-requirements.txt
pip install -e .  # Instalar el proyecto (necesario para mkdocstrings)

# Servir localmente con hot-reload
mkdocs serve
# Abrí http://127.0.0.1:8000
```

## Convenciones de docstrings

Usá docstrings en **estilo Google**. `mkdocstrings` los renderizará automáticamente.

```python
def calcular_cosa(x: float, y: float, metodo: str = "rapido") -> float:
    """Calcula la cosa usando el método especificado.

    Esta función hace algo útil que merece
    una explicación más larga en varias líneas.

    Args:
        x: El primer valor de entrada.
        y: El segundo valor de entrada.
        metodo: Algoritmo a utilizar. Uno de `"rapido"`, `"preciso"`.

    Returns:
        El resultado calculado.

    Raises:
        ValueError: Si `metodo` no es reconocido.

    Example:
        ```python
        resultado = calcular_cosa(1.0, 2.0, metodo="preciso")
        ```
    """
```

## Agregar una nueva página de documentación

1. Creá un archivo `.md` en el subdirectorio adecuado de `docs/`
2. Agregalo a la sección `nav:` en `mkdocs.yml`
3. Si es una página de referencia de API, se genera automáticamente — solo escribí los docstrings

## Despliegue en ReadTheDocs

El despliegue es automático:
- Cada push a `main` reconstruye la documentación **latest**
- Cada release con tag construye una versión **versionada**
- Los PRs reciben una **previsualización** (configurada en `.readthedocs.yaml`)

## Notas de compatibilidad con Obsidian

La carpeta `docs/` está diseñada para abrirse como un vault de Obsidian.
Los colaboradores no técnicos la editan de esa manera. Por favor:

- **No** agregues archivos a `docs/` que rompan la estructura del vault de Obsidian
- **No** uses sintaxis que solo se renderiza en MkDocs pero se ve mal en Obsidian
- **Sí** mantené el directorio `docs/.obsidian/` ignorado en git
- **Sí** verificá que tus cambios se rendericen correctamente tanto en `mkdocs serve` como en Obsidian
