# -*- coding: utf-8 -*-
#pylint: disable=C0301
"""
>>> import secrecy
>>> data = bytearray(b'1234abcdABCD@#~00')
>>> data[-2] = 0x00 #Nulls don't terminate
>>> data[-1] = 0xFF #Non ASCII preserved
>>> secrecy.dec(secrecy.enc(bytes(data))) == data
True
>>> secrecy.enc(bytes(data)) == data #At least not a no-op
False
"""
from __future__ import division, absolute_import, print_function, unicode_literals
