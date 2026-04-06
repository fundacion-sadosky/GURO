---
title: Contributing (for developers)
---

# Contributing (for developers)

## Documentation stack

| Component | Purpose |
|---|---|
| [MkDocs](https://www.mkdocs.org/) | Static site generator |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Visual theme |
| [mkdocstrings](https://mkdocstrings.github.io/) | Automatic API documentation from docstrings |
| [mkdocs-obsidian-bridge](https://github.com/GooRoo/mkdocs-obsidian-bridge) | Obsidian wikilinks support (fallback) |
| [mkdocs-gen-files](https://github.com/oprypin/mkdocs-gen-files) | Automatic generation of reference pages |

## Local development

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install documentation dependencies
pip install -r docs-requirements.txt
pip install -e .  # Install the project (needed for mkdocstrings)

# Serve locally with hot-reload
mkdocs serve
# Open http://127.0.0.1:8000
```

## Docstring conventions

Use **Google-style** docstrings. `mkdocstrings` will render them automatically.

```python
def calculate_thing(x: float, y: float, method: str = "fast") -> float:
    """Calculates the thing using the specified method.

    This function does something useful that deserves
    a longer explanation across multiple lines.

    Args:
        x: The first input value.
        y: The second input value.
        method: Algorithm to use. One of `"fast"`, `"precise"`.

    Returns:
        The calculated result.

    Raises:
        ValueError: If `method` is not recognized.

    Example:
        ```python
        result = calculate_thing(1.0, 2.0, method="precise")
        ```
    """
```

## Adding a new documentation page

1. Create a `.md` file in the appropriate subdirectory of `docs/`
2. Add it to the `nav:` section in `mkdocs.yml`
3. If it is an API reference page, it is generated automatically — just write the docstrings

## Deployment on ReadTheDocs

Deployment is automatic:
- Every push to `main` rebuilds the **latest** documentation
- Every release with a tag builds a **versioned** version
- PRs receive a **preview** (configured in `.readthedocs.yaml`)

## Obsidian compatibility notes

The `docs/` folder is designed to be opened as an Obsidian vault.
Non-technical collaborators edit it that way. Please:

- **Do not** add files to `docs/` that break the Obsidian vault structure
- **Do not** use syntax that only renders in MkDocs but looks bad in Obsidian
- **Do** keep the `docs/.obsidian/` directory ignored in git
- **Do** verify that your changes render correctly in both `mkdocs serve` and Obsidian
