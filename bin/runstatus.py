#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""
:References:
    `coverage <../../../cover/bin_runstatus.html>`_

Run the display
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
import logger
LOG = logger.Log(__file__)

import status

def main():
    disp = status.Status()
    disp.run()
          
if __name__ == "__main__":
    main()
