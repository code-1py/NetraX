import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

with (ROOT / "pyproject.toml").open("rb") as project_file:
    project_metadata = tomllib.load(project_file)["project"]

project = project_metadata["name"]
author = ", ".join(item["name"] for item in project_metadata.get("authors", []))
copyright = f"2026, {author}"
release = project_metadata["version"]
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autosummary_generate = True
autodoc_member_order = "bysource"
autodoc_typehints = "description"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
root_doc = "index"
html_theme = "furo"
html_title = f"{project} {version} documentation"
html_static_path = []
html_show_sourcelink = False
