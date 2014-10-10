import sys
import os

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon',
    'sphinxcontrib.restbuilder'
]

source_suffix = '.rst'
master_doc = 'index'
project = u'bprofile'
copyright = u'2014, Chris Billington'
version = '1.1'
release = '1.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

# html
html_theme = 'default'
htmlhelp_basename = 'bprofiledoc'

# latex
latex_documents = [('index', 'bprofile.tex', u'bprofile Documentation', u'Chris Billington', 'manual')]

