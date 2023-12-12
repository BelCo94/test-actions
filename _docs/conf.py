project = 'TEST'
copyright = 'TEST'
author = 'TEST'

extensions = ['breathe']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
}

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

def setup(app):
    app.srcdir = 'source'
