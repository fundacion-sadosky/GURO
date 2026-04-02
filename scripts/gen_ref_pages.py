"""Generate the code reference pages and navigation.

This script is executed by mkdocs-gen-files during `mkdocs build`.
It walks the Python package and creates a markdown page per module,
using mkdocstrings to render the docstrings.

Technical contributors maintain docstrings in code.
This script turns them into browsable docs automatically.
"""

from pathlib import Path
import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

package_dir = Path("src")

for path in sorted(package_dir.rglob("*.py")):
    module_path = path.relative_to("src").with_suffix("")
    doc_path = path.relative_to("src").with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    # Skip __main__ and private modules
    if parts[-1] == "__main__":
        continue
    if any(part.startswith("_") and part != "__init__" for part in parts):
        continue

    # Clean up __init__ modules
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")

    if not parts:
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path.as_posix())

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
