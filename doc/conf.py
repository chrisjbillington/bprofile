import sys
import os

sys.path.insert(0, os.path.abspath('..'))

# Pull the version string out of setup.py without importing it
with open('../setup.py') as f:
    for line in f:
        if '__version__' in line:
            __version__ = eval(line.split('=')[1])
            break

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

if os.environ.get('READTHEDOCS', None) is None:
    # For making the README.rst file with 'make readme':
    extensions.append('sphinxcontrib.restbuilder')

master_doc = 'index'
project = u'bprofile'
copyright = u'2014, Chris Billington'
version = __version__
release = '.'.join(__version__.split('.')[:-1])
