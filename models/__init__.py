# -*- coding: utf-8 -*-
"""
Models
======

Securly store and retrieve target data.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    :doc:`models.test`
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import settings
from .security import encode, decode_sector
from .storage import Target, TargetStore
from Crypto import Random

class Block(object):
    """16 bytes of data"""
    _has_uid = False

    def __init__(self, uid = None):
        """Initalize with 0xFF (to match factory tokens)"""
        self._has_uid = uid != None
        if self._has_uid:
            self.data = uid + b'\xFF' * 12
        else:
            self.data = b'\xFF' * 16

    def randomize(self):
        """Fill with random values"""
        if self._has_uid:
            self.data = self.data[:4] + Random.get_random_bytes(12)
        else:
            self.data = Random.get_random_bytes(16)

    def uid(self):
        """If this is the first block return the contained UID"""
        if self._has_uid:
            return ''.join([hex(char) for char in bytearray(self.data[:4])])
        else:
            raise Exception('No UID')

class Sector(object):
    """Three :py:class:`block` followed by a 6 byte key, 4 bytes of access permissions, and another key"""
    key_a = b'\xFF' * 6
    access = b'\xFF\x07\x80\x69'
    key_b =  b'\xFF' * 6

    def __init__(self, uid = None):
        """Create blocks"""
        self.blocks = [Block(uid), Block(), Block()]

    def randomize(self):
        """Randomise keys and blocks"""
        for block in self.blocks:
            block.randomize()
        self.key_a = Random.get_random_bytes(6)
        self.key_b = Random.get_random_bytes(6)

    def raw(self):
        """Return all data"""
        buf = b''
        for block in self.blocks:
            buf += block.data
        buf += self.key_a
        buf += self.access
        buf += self.key_b
        return buf

    def load(self, data):
        """Load data into sector"""
        self.blocks[0].data = data[0:16]
        self.blocks[1].data = data[16:32]
        self.blocks[2].data = data[32:48]
        self.key_a = data[48:54]
        self.access = data[54:58]
        self.key_b = data[58:64]

class Token(object):
    """A 1k Mifare card with 16 :py:class:`sector`"""
    _can_save = True

    def __init__(self, uid):
        """All tokens must have a uid"""
        self.sectors = [
            Sector(uid), Sector(), Sector(), Sector(), Sector(), Sector(), Sector(), Sector(),
            Sector(), Sector(), Sector(), Sector(), Sector(), Sector(), Sector(), Sector()
        ]

    def randomize(self):
        """generate cryptographic quality random keys and random data which can securly initialise a new target."""
        for sector in self.sectors:
            sector.randomize()

    def raw(self):
        """Return all data"""
        buf = b''
        for sector in self.sectors:
            buf += sector.raw()
        return buf

    def uid(self):
        """Return the UID"""
        return self.sectors[0].blocks[0].uid()  

    def load(self, sector = settings.SECTOR):
        """Load a single, configuration defined, sector from storage"""
        self._can_save = False
        self.sectors[sector].load(
            decode_sector(
                Target(
                    TargetStore(),
                    self.uid()
                ).read(),
                sector
            )
        )

    def save(self):
        """Save to (encrypted) storage"""
        if not(self._can_save):
            raise Exception("Don't overwrite existing tokens.")
        Target(
            TargetStore(),
            self.uid()
        ).write(
            encode(
                self.raw()
            )
        )
