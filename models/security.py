# -*- coding: utf-8 -*-
"""
Security
--------

Use a seperate public key to encript each sector of the card before we store it.

This should allow 16 independent applications to share a card securly.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
"""
from __future__ import division, absolute_import, print_function, unicode_literals

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import settings

def _enc(buf, sector):
    """PKCS#1 OAEP encrypt a sector"""
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

def decode_sector(token, sector = settings.SECTOR):
    """Ready a sector of an encripted token for use"""
    return _dec(token[sector * 512:(sector+1) * 512])

def encode(token):
    """Encrypt a token for storage"""
    buf = b''
    for sector in range(16):
        buf += _enc(token[sector * 64:(sector+1) * 64], sector)
    return buf
