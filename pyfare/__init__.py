# -*- coding: utf-8 -*-
"""
PyFare
======

Support for Mifare RFID communications via popular reader chips.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    `pylint <../../../cover/pyfare.lint.html>`_,
    `coverage <../../../cover/pyfare___init__.html>`_,
    :doc:`hd44780.test`
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import logger
LOG = logger.Log(__file__)
import serial
from .pn532 import PN532
from .sm130 import SM130
import settings
from Crypto import Random

_ACCESS = b'\xFF\x07\x80\x69'

def _block_offset(sector, block):
    """Get the offset of a given block. Assumes Sector = 4 * 16 byte blocks (Mifare)."""
    return sector * 4 * 16 + block * 16

def _key(data, sector, key_b = False):
    """Return a key from the given data."""
    return data[_block_offset(sector, 3) + key_b * 10: _block_offset(sector, 3) + key_b * 10 + 6]

def _block(data, sector, block):
    """Return a block from the given data."""
    return data[_block_offset(sector, block): _block_offset(sector, block + 1)]


class NFC(object):
    """Object for controlling NFC/RFID devices and via them targets (cards etc.)."""

    def __init__(self, connection):
        """Open commumnications with specified device"""
        self._reader = globals()[connection[0]](serial.Serial(*connection[1:]))

    def waitfortarget(self):
        """Wait for a target to enter the field, subsiquent commands are sent to this target."""
        return self._reader.waitfortarget()

    def wait_1s_fortarget(self):
        """Wait for a target to enter the field, subsiquent commands are sent to this target."""
        return self._reader.wait_1s_fortarget()

    def unlock(self):
        return self._reader.unlock()

    def blank(self, uid):
        """Return the factory keys for authenticating with new targets."""
        return uid + b'\xFF' * 1020

    def generate(self, uid):
        """Generate cryptographic quality random keys and random data which can securly initialise a new target."""
        for sector in range(16):
            if sector == 0:
                buf = uid + Random.get_random_bytes(-4 + 3 * 16 + 6)
            else:
                buf += Random.get_random_bytes(3 * 16 + 6)
            buf += _ACCESS
            buf += Random.get_random_bytes(6)
        return buf

    def verify(self, data):
        """
        Verify that the current target matches the data.

        Authenticates then reads the first block form the sector and compares with stored value.
        """
        if self._reader.auth(settings.SECTOR * 4, _key(data, settings.SECTOR)):
            buf = self._reader.read(settings.SECTOR * 4)
            if buf != None:
                return buf == _block(data, settings.SECTOR, 0)
        else:
            return False

    def write_all(self, olddata, data):
        """
        Write all data data to the current target

        If the write partially succedes it will return false and `olddata` will be updated with any succesfully written keys.
        """
        LOG.debug('Writing card')
        for sector in reversed(range(16)):
            #Auth with old key
            if self._reader.auth(sector * 4 + 3, _key(olddata, sector)):
                #Write new trailier, including new keys
                if self._reader.write(sector * 4 + 3, _block(data, sector, 3)):
                    #If we wrote new keys update the olddata incase somthing else fails
                    olddata[_block_offset(sector, 3): _block_offset(sector, 4)] = _block(data, sector, 3)
                    #Re-auth with new key
                    if self._reader.auth(sector * 4 + 3, _key(data, sector)):
                        for block in range(4):
                            if sector != 0 or block != 0:
                                self._reader.write(sector * 4 + block, _block(data, sector, block))
                    else:
                        return False
                else:
                    return False
            else:
                return False

