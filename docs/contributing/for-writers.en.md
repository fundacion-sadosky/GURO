---
title: Documentation contributions (for writers)
---

# Documentation contributions

You don't need to be a programmer to contribute to this project's documentation.
All you need is [Obsidian](https://obsidian.md) (free) and a GitHub account.

## Initial setup (~5 minutes)

1. **Fork** this repository on GitHub
2. **Clone** the repository to your computer
3. Open the `docs/` folder as an **Obsidian vault**
   (`File → Open vault → Open folder as vault → select docs/`)
4. In Obsidian, go to `Settings → Files and links`:
    - Set **Default location for new notes** → `Same folder as current file`
    - **Disable** `Use [[Wikilinks]]` → use standard Markdown links
    - Set **New link format** → `Relative path to file`

> [!tip] Why disable wikilinks?
> Standard Markdown links (`[text](file.md)`) work everywhere:
> in Obsidian, on GitHub, and on the documentation site.
> Wikilinks (`[[file]]`) only work in Obsidian.

## Writing conventions

### What you can use freely

These features behave the same way in Obsidian and on the published site:

- **Headings** (`# H1` through `#### H4`)
- **Bold**, *italic*, ~~strikethrough~~, ==highlight==
- Standard Markdown links: `[link text](another-page.md)`
- Images: `![alt text](assets/image.png)`
- Code blocks with syntax highlighting
- Tables
- Task lists (`- [ ] pending`)
- Mermaid diagrams (inside ` ```mermaid ` blocks)
- LaTeX math: `$inline$` and `$$block$$`
- Callouts / admonitions:

```text
> [!note] Title here
> Body text here.
>
> Supports **formatting** and `code`.
```

Available callout types: `note`, `tip`, `warning`, `danger`, `example`,
`question`, `quote`, `info`, `bug`, `success`, `failure`, `abstract`.

### What to avoid

| Feature | Why | Alternative |
|---|---|---|
| `[[wikilinks]]` | Not portable | `[text](file.md)` |
| `![[embed]]` | Not portable | Copy the relevant text or link to it |
| `^block-references` | Not portable | Use heading links: `[text](file.md#heading)` |
| Obsidian-only plugins | Do not render on the site | Use standard Markdown |

## How to submit your changes

1. Create a new **branch** for your changes
2. Write or edit the `.md` files inside `docs/`
3. **Commit** and **push** to your fork
4. Open a **Pull Request** on GitHub
5. The documentation will be compiled and previewed automatically

> [!tip] Preview before submitting
> You can see exactly how the documentation will look on the site.
> Ask a developer for help running `mkdocs serve` locally,
> or check the PR preview on ReadTheDocs.
