#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""
:References:
    `coverage <../../../cover/bin_mcp.html>`_

Handle the locking/unlocking state machine
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
import logger
LOG = logger.Log(__file__)

import datetime
import time
import settings

LOCKED = 0
UNLOCKING = 1
OPENING = 2
OPEN = 3
LOCKING = 4
LOCKING_WARN = 5
LOCKING_FAIL = 6

def door_open():
    """Return if the door is adjar"""
    #TODO
    return False

# Unushal style appropriate here #pylint: disable=R0912,R0915
def main():
    """Implements the door's FSM and timeouts."""

    lastunlock = time.clock()
    bolts = []
    locks = []
    status = LOCKING

    while True:

        if os.path.getmtime('SESAME') > lastunlock:
            lastunlock = os.path.getmtime('SESAME')
            status = UNLOCKING
            deadline = None
            deadline = datetime.datetime.now() + settings.DEADLINE_OPENING
            LOG.info("unlocking")
            for bolt in bolts:
                bolt.unlock()
            for lock in locks:
                lock.unlock()
    
        if door_open():

            if status == LOCKED:
                status = LOCKING_FAIL
                deadline = None
                LOG.error("Lock fail")
                #Try and recover
                for bolt in bolts:
                    bolt.unlock()

            if status == UNLOCKING or status == OPENING:
                status = OPEN
                #Don't change deadline

            if status == OPEN:
                if deadline < datetime.datetime.now():
                    status = LOCKING
                    deadline = datetime.datetime.now() + settings.DEADLINE_LOCKING

            if status == LOCKING:
                if deadline < datetime.datetime.now():
                    status = LOCKING_WARN
                    deadline = datetime.datetime.now() + settings.DEADLINE_LOCKING_WARN
                    LOG.info("please close door")
                    #TODO

            if status == LOCKING_WARN:
                if deadline != None and deadline < datetime.datetime.now():
                    status = LOCKING_FAIL
                    deadline = None
                    LOG.error("locking fail")
                    #Try and recover
                    for bolt in bolts:
                        bolt.unlock()
                    #TODO

        else:
            if status == UNLOCKING:
                pass

            if status == OPENING:
                if deadline < datetime.datetime.now():
                    status = LOCKING
                    deadline = datetime.datetime.now() + settings.DEADLINE_LOCKING
                    LOG.warn("unlock without open")
            
            if status == OPEN:
                LOG.info("door closed, locking")
                status = LOCKING
                deadline = datetime.datetime.now() + settings.DEADLINE_LOCKING

            if status == LOCKING or status == LOCKING_WARN or status == LOCKING_FAIL:
                status = LOCKED
                deadline = None
                if status == LOCKING_FAIL:
                    LOG.error("relocked after fail")
                else:
                    LOG.info('locking')
                for bolt in bolts:
                    bolt.lock()
                for lock in locks:
                    lock.lock()

        time.sleep(1)
          
if __name__ == "__main__":
    main()
