"""Sphinx configuration file."""

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'NAMMI'
copyright = '2024, John Koumoulas'
author = 'John Koumoulas'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'manim': ('https://docs.manim.community/en/stable/', None),
} 