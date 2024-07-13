# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sphinx_readable_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Molduck"
copyright = "2024, Giulio De Matteis"
author = "Giulio De Matteis"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.httpdomain",
    "sphinx_multiversion",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "readable"
html_sidebars = {
    "**": [
        "projectname.html",
        "navigation.html",
        "localtoc.html",
        "searchbox.html",
        "versioning.html",
    ]
}
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_show_sourcelink = False
html_static_path = ["_static"]

master_doc = "index"

smv_remote_whitelist = r"^origin$"
smv_branch_whitelist = r"^master$"
