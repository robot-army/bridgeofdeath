#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
import logger
LOG = logger.Log(__file__)

import time
import hd44780

def main():
    s = hd44780.Screen()
    s.widgets.append(hd44780.Static(s, hd44780.Coord(1, 0), hd44780.Coord(14, 1)))
    while True:
        s.widgets[0].write(time.strftime("%m-%d %H:%M:%S", time.localtime()))
        s.render()
        s.send()
        time.sleep(1)

if __name__ == "__main__":
    main()
