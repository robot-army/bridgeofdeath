#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""

:References:
    `coverage <../../../cover/binread_token.html>`_

Read NFC tokens
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import sys
import shutil
import os
sys.path.append('/home/gilliam/bridgeofdeath')
import time
import logger
LOG = logger.Log(__file__)
import pyfare
import models
import settings
import requests

def _touch(fname, times=None):
    """Change a files modification time"""
    with file(fname, 'a'):
        os.utime(fname, times)

def _id(target):
    """Format binary uid for storage/lookup"""
    return ''.join([hex(char) for char in bytearray(target)])

def _idprint(target):
    """Format binary uid for storage/lookup"""
    return ''.join(["%02X" % char for char in bytearray(target)])



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
            LOG.info("Reading card: " + _idprint(target))

        #Check for valid card
        try:
            with open('/home/gilliam/bridgeofdeath/' + _id(target) + '.dat', 'rb') as infile:
                token = infile.read()
            valid = True
        except IOError:
            pass
        else:
            if nfc.verify(token):
                LOG.info("Valid card")
                bad = None, None
                http = requests.get('https://members.rlab.org.uk/member/name/',auth=(_idprint(target),''),cert='/home/gilliam/client.pem')
                LOG.info("Member name: " + http.text)
                #_touch('SESAME')
                #nfc.unlock()

                #Check for magic three card sequence to auth a new card
                if prevprev[2] and not(prev[2]) and prevprev[0] > time.time()-6 and prevprev[1] == _id(target):
                    LOG.info("Three card sequence")
                    try:
                        open('/home/gilliam/bridgeofdeath/admin/' + _id(target) + '.dat', 'rb')
                        LOG.info("Admin card")
                        try:
                            shutil.move('/home/gilliam/bridgeofdeath/new/' + prev[1] + '.dat', '/home/gilliam/bridgeofdeath/' + prev[1] + '.dat')
                            LOG.info("New card authorized:" + prev[1])
                        except:
                            LOG.warn("Not pre-authed card")
                    except IOError:
                        LOG.info("Not admin")

        #Track last two cards for magic three card sequence
        if prev[1] != _id(target) or prev[0] < time.time()-3 or prev[2] != valid:
            prevprev = prev
            prev = time.time(), _id(target), valid


def deamonize():
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
            sys.exit(1)

    os.chdir("/")
    os.setsid()
    os.umask(0)
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        sys.exit(1)

if __name__ == "__main__":
#    deamonize()
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
