# -*- coding: utf-8 -*-
"""
Fake RFID module.
"""
from __future__ import division, absolute_import, print_function, unicode_literals

class Mock(object):
    """
    Fake RFID module.
    """
    _target = None

    def __init__(self, serial):
        """Check we are talking to a known firmware."""
        self._serial = serial

    #pylint: disable-msg=W0613
    def auth(self, block, key, key_a = True):
        """Attempt to authenticate a block on current target"""
        return False

    #pylint: disable-msg=W0613
    def read(self, block):
        """Read block"""
        return b'\xFF' * 16

    #pylint: disable-msg=W0613
    def write(self, block, data):
        """Write block"""
        return True

    #pylint: disable-msg=W0613
    def waitfortarget(self):
        """Wait until a target enters the field"""
        return b'\xFF\xFF\xFF\xFF'

    def unlock(self):
        """Fire the reader's GPIO (to trigger door lock)"""
        return True
