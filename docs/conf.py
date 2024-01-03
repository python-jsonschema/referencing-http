import importlib.metadata
import re

project = "referencing-http"
author = "Julian Berman"
copyright = f"2024, {author}"

release = importlib.metadata.version("referencing-http")
version = release.partition("-")[0]

language = "en"
default_role = "any"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.spelling",
    "sphinxext.opengraph",
]

pygments_style = "lovelace"
pygments_dark_style = "one-dark"

html_theme = "furo"


def entire_domain(host):
    return r"http.?://" + re.escape(host) + r"($|/.*)"


linkcheck_ignore = [
    entire_domain("img.shields.io"),
    "https://github.com/Julian/referencing-http/actions",
    "https://github.com/Julian/referencing-http/workflows/CI/badge.svg",
    # REMOVEME: Once a release is out.
    "https://pypi.org/project/referencing-http/",
    entire_domain("referencing-http.readthedocs.io"),
]

# = Extensions =

# -- autosectionlabel --

autosectionlabel_prefix_document = True

# -- sphinxcontrib-spelling --

spelling_word_list_filename = "spelling-wordlist.txt"
spelling_show_suggestions = True
