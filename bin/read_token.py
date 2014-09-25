#! python
# -*- coding: utf-8 -*-
"""

:References:
    `coverage <../../../cover/binread_token.html>`_

Read NFC tokens
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import shutil
import os
import time
import logger
LOG = logger.Log(__file__)
import pyfare
import models
import settings

def _id(target):
    """Format binary uid for storage/lookup"""
    return ''.join([hex(char) for char in bytearray(target)])

def main():
    """Waits in an infinate loop for targets to enter field, then checks if they are trusted."""
    nfc = pyfare.NFC(settings.ENTER)
    prev = None, None, None
    prevprev = None, None, None
    while True:
        target = nfc.waitfortarget()

        #3s cool down for same card after valid
        if prev[2] and prev[0] > time.time()-3 and prev[1] == _id(target):
            continue

        #Throttle logs for retries
        if prev[0] < time.time()-3 or prev[1] != _id(target):
            LOG.info("Reading card: " + _id(target))

        #Check for valid card
        valid = False
        try:
            token = models.Token(target)
            token.load()
            LOG.info("Found card")
        except IOError:
            pass
        else:
            if nfc.verify(token):
                LOG.info("Valid card")
                bad = None, None

                nfc.unlock()

                #Check for magic three card sequence to auth a new card
                if prevprev[2] and not(prev[2]) and prevprev[0] > time.time()-6 and prevprev[1] == _id(target):
                    LOG.info("Three card sequence")
                    try:
                        open(_id(target) + '.dat', 'rb')
                        LOG.info("Admin card")
                        try:
                            shutil.move('new/' + prev[1] + '.dat', prev[1] + '.dat')
                            LOG.info("New card authorized:" + prev[1])
                        except:
                            LOG.warn("Not pre-authed card")
                    except IOError:
                        LOG.info("Not admin")

        #Track last two cards for magic three card sequence
        if prev[1] != _id(target) or prev[0] < time.time()-3 or prev[2] != valid:
            prevprev = prev
            prev = time.time(), _id(target), valid

if __name__ == "__main__":
    main()

