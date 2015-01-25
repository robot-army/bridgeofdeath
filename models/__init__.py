# -*- coding: utf-8 -*-
"""
Secrecy
=======

Use a seperate public key to encript each sector of the card before we store it.

This should allow 16 independent applications to share a card securly.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    `pylint <../../../cover/secrecy.lint.html>`_,
    `coverage <../../../cover/secrecy___init__.html>`_,
    :doc:`secrecy.test`
"""
from __future__ import division, absolute_import, print_function, unicode_literals

class Block(object):
    _has_uid = False

    def __init__(self, uid = None):
        self._has_uid = uid != None
        if self._has_uid:
            self.data = uid + b'\xFF' * 12
        else:
            self.data = b'\xFF' * 16

    def randomize(self):
        if self._has_uid:
            self.data = self.data[:4] + Random.get_random_bytes(12)
        else:
            self.data = Random.get_random_bytes(16)

    def uid(self):
        if self._has_uid:
            return self.data[:4]
        else:
            raise Exception('No UID')

class Sector(object):
    key_a = b'\xFF' * 6
    access = b'\xFF\x07\x80\x69'
    key_b =  b'\xFF' * 6

    def __init__(self, uid = None):
        self.blocks = [Block(uid)] + [Block()] * 2

    def randomize(self):
        for block in self.blocks:
            block.randomize()
        self.key_a = Random.get_random_bytes(6)
        self.key_b = Random.get_random_bytes(6)

    def raw(self):
        buf = b''
        for block in self.blocks:
            buf += block.data
        buf += self.key_a
        buf += self.access
        buf += self.key_b
        return buf

    def load(self, data):
        self.block[0].data = data[0:16]
        self.block[1].data = data[16:32]
        self.block[2].data = data[32:48]
        self.key_a = data[48:54]
        self.access = data[54:58]
        self.key_b = data[58:64]

class Token(object):
    """A 1k Mifare card"""
    sectors = [Sector() for _ in range(16)]

    def __init__(self, uid):
        """All tokens must have a uid"""
        self.sectors = [Sector(uid)] + [Sector()] * 15

    def randomize(self):
        """generate cryptographic quality random keys and random data which can securly initialise a new target."""
        for sector in self.sectors:
            sector.randomize()

    def raw(self):
        buf = b''
        for sector in self.sectors:
            buf += sector.raw()
        return buf

    def uid():
        return self.sectors[0].block[0].uid()

    def load(self, sector = settings.SECTOR):
        #todo find by uid
        #todo decrypt
        self.sectors[sector].load(data)

from Crypto.PublicKey import RSA
import settings

def _enc(buf, sector):
    """PKCS#1 OAEP encrypt a sector (skiping the uid on the first sector)"""
    if sector == 0:
        return buf[:4] + PKCS1_OAEP.new(
                RSA.importKey(
                    settings.PUBLIC_KEYS[sector][1:]
                )
            ).encrypt(buf[4:])
    else:
        return PKCS1_OAEP.new(
            RSA.importKey(
                settings.PUBLIC_KEYS[sector][1:]
            )
        ).encrypt(buf)

def _dec(buf):
    """PKCS#1 OAEP decrypt a sector"""
    return PKCS1_OAEP.new(
        RSA.importKey(
            open('private.pem').read()
        )
    ).decrypt(buf)

def _off(sector):
    """Return the sector's offset"""
    return sector * 64

def dec(token, sector = settings.SECTOR):
    """Ready an encripted token for use"""
    return token[:_off(sector)] +
        _dec(token[_off(sector):_off(sector+1)]) +
        token[_off(sector+1):]

def enc_token(token):
    """Encrypt a token for storage"""
    buf = b''
    for sector in range(16):
        buf += _enc(token[_off(sector):_off(sector+1)], sector)
    return buf
