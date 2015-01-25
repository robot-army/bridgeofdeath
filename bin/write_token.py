#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""

:References:
    `coverage <../../../cover/bin_write_token.html>`_

Write a new NFC token.
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
import logger
LOG = logger.Log(__file__)
import pyfare
import settings

def _id(target):
    """Format binary uid for storage/lookup"""
    return ''.join([hex(char) for char in bytearray(target)])

def main():
    """
    Write new random data to a blank token and store that it is trusted.
    Please put the card in the field prior to writing to ensure best chance of success.
    n.b. failed writes can be recovered from `_RECOVER_.dat` (or mfoc if you loose that)
    """
    nfc = pyfare.NFC(settings.ENTER)
    target = nfc.waitfortarget()
    LOG.info("Writing card: " + _id(target))
    #TODO: secrecy and ldap
    with open(_id(target) + '.dat', 'wb') as output:
        oldtoken = bytearray(nfc.blank(target))
        token = nfc.generate(target)
        output.write(token)
        success = False       
        try:
            success = nfc.write_all(oldtoken, token)
        finally:
            if not(success):
                with open('_RECOVER_.dat', 'wb') as recover:
                    recover.write(oldtoken)

if __name__ == "__main__":
    main()
