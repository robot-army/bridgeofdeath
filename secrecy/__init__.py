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
from Crypto.Cipher import PKCS1_OAEP
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
