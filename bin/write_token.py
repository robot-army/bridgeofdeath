#! /usr/bin/python
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
import models
import settings

def main():
    """
    Write new random data to a blank token and store that it is trusted.
    Please put the card in the field prior to writing to ensure best chance of success.
    n.b. failed writes can be recovered from `_RECOVER_.dat` (or mfoc if you loose that)
    """
    nfc = pyfare.NFC(settings.ENTER)
    target = nfc.waitfortarget()
    token = models.Token(target)
    oldtoken = models.Token(target)
    token.randomize()
    LOG.info("Writing card: " + token.uid())
    token.save()
    nfc.write_all(oldtoken, token)

if __name__ == "__main__":
    main()
