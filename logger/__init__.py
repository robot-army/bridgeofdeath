# -*- coding: utf-8 -*-
"""
Logger
======

We need very paranoid logging as everything must work first time.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    `pylint <../../../cover/logger.lint.html>`_,
    `coverage <../../../cover/logger___init__.html>`_
    :doc:`logger.test`
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import sys
import logging
import logging.handlers
import settings
import types

def _debug_hex(self, data):
    """Helper to nicely format long binary logs"""
    data = data.encode('hex')
    buf = ''
    for i in range(0, len(data), 16):
        buf += data[i:i + 16] + ' '
        if i % 64 == 64-16:
            buf += '\n'
    self.debug(buf)

#Pretend to be a class #pylint: disable=C0103
def Log(name):
    """Factory to create a logger preconfigured to our liking"""
    self = logging.getLogger(name)
    self.debug_hex = types.MethodType(_debug_hex, self)
    self.setLevel(logging.DEBUG)
    syslog = logging.handlers.SysLogHandler('/dev/log')
    syslog.setLevel(logging.DEBUG)
    self.addHandler(syslog)
    maillog = logging.handlers.SMTPHandler(
        settings.EMAIL_SERVER,
        settings.EMAIL_FROM,
        settings.EMAIL_ERRORS_TO,
        name
    )
    maillog.setLevel(logging.ERROR)
    self.addHandler(maillog)
    #console = logging.StreamHandler()
    #console.setLevel(logging.DEBUG)
    #self.addHandler(console)
    #sys.excepthook = lambda *exc_info: self.error("Unhandled exception:", exc_info=exc_info) # pragma: no cover
    return self
