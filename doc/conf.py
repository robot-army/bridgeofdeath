# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage', 
    'sphinx.ext.viewcode'
]

master_doc = 'index'

project = 'Bridge of Death'
copyright = '2013 Reading Makerspace Ltd'
version = '0.1'
release = '0.1'

intersphinx_mapping = {
    'http://docs.python.org/': None
}

todo_include_todos = True

autodoc_default_flags = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance'
]
