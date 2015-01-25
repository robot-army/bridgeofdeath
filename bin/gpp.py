#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""
:References:
    `coverage <../../../cover/bin_gpp.html>`_

Provide user feedback
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import logger
LOG = logger.Log(__file__)

import hd44780
import datetime
import time

def formattime():
    """Format current time for LCD"""
    return datetime.datetime.now().strftime('%H%M')

def main():
    """Updates the LCD"""
    screen = hd44780.Screen()

    heartbeat = hd44780.Animated(screen, hd44780.Coord(15, 1), hd44780.Coord(1, 1))
    heartbeat.write('*')
    heartbeat.write(' ')
    screen.widgets.append(heartbeat)

    msg = hd44780.Animated(screen, hd44780.Coord(5, 0), hd44780.Coord(10, 2))
    screen.widgets.append(msg)

    status = hd44780.Static(screen, hd44780.Coord(0, 1), hd44780.Coord(4, 1))
    status.write('LOCK')
    screen.widgets.append(status)

    clock = hd44780.Static(screen, hd44780.Coord(0, 0), hd44780.Coord(4, 1))
    screen.widgets.append(clock)

    while True:
        clock.write(formattime())
        screen.render()
        time.sleep(1)

    
if __name__ == "__main__":
    main()
