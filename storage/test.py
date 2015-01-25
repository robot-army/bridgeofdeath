# -*- coding: utf-8 -*-
#pylint: disable=C0301
"""
>>> import storage
>>> import settings
>>> store = storage.TargetStore()
>>> target = storage.Target(store, 'TEST')
>>> target.read()
'1234'
>>> target.write(b'1234')
>>> target = storage.Target(store, 'FAIL')
>>> target.read() #doctest: +ELLIPSIS
Traceback (most recent call last):
NO_SUCH_OBJECT: {'matched': '...', 'desc': 'No such object'}
>>> del target
>>> del store
"""
from __future__ import division, absolute_import, print_function, unicode_literals
