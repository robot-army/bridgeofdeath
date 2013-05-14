# -*- coding: utf-8 -*-
"""
PyFare
======

Support for Mifare RFID communications via popular reader chips.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    :doc:`pyfare.test`
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import logger
LOG = logger.Log(__file__)
import serial
from .mock import Mock
from .pn532 import PN532
from .sm130 import SM130
import settings

_ACCESS = b'\xFF\x07\x80\x69'

class NFC(object):
    """Object for controlling NFC/RFID devices and via them targets (cards etc.)."""

    def __init__(self, connection):
        """Open commumnications with specified device"""
        self._reader = globals()[connection[0]](serial.Serial(*connection[1:]) if connection[0] != 'Mock' else None)

    def waitfortarget(self):
        """Wait for a target to enter the field, subsiquent commands are sent to this target."""
        return self._reader.waitfortarget()

    def unlock(self):
        """Fire the readers GPIO (to trigger door lock)"""
        return self._reader.unlock()

    def verify(self, token):
        """
        Verify that the current target matches the data.

        Authenticates then reads the first block form the sector and compares with stored value.
        """
        if self._reader.auth(settings.SECTOR * 4, token.sectors[settings.SECTOR].key_a):
            buf = self._reader.read(settings.SECTOR * 4)
            if buf != None:
                return buf == token.sectors[settings.SECTOR].block[0]
        else:
            return False

    def write_all(self, oldtoken, token):
        """
        Write all data data to the current target

        If the write partially succedes it will return false and `olddata` will be updated with any succesfully written keys.
        """
        LOG.debug('Writing card')
        for sector in reversed(range(16)):
            #Auth with old key
            if self._reader.auth(
                sector * 4 + 3,
                oldtoken.sectors[sector].key_a
            ):
                #Write new trailier, including new keys
                if self._reader.write(
                    sector * 4 + 3,
                    token.sectors[sector].key_a +
                        token.sectors[sector].access +
                            token.sectors[sector].key_b
                ):
                    #If we wrote new keys update the olddata incase somthing else fails
                    oldtoken.sectors[sector].key_a = token.sectors[sector].key_a
                    oldtoken.sectors[sector].access = token.sectors[sector].access
                    oldtoken.sectors[sector].key_b = token.sectors[sector].key_b
                    #Re-auth with new key
                    if self._reader.auth(
                        sector * 4 + 3,
                        token.sector[sector].key_a
                    ):
                        for block in range(3):
                            if sector != 0 or block != 0:
                                self._reader.write(sector * 4 + block, token.sectors[sector].blocks[block].data)
                    else:
                        return False
                else:
                    return False
            else:
                return False

