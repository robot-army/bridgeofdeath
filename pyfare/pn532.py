# -*- coding: utf-8 -*-
"""
NPX PN532 NFC controller.
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import time

class PN532(object):
    """
    NPX PN532 NFC controller.
    """
    _target = None
    _logical_target = None

    def __init__(self, serial):
        """Send wakeup and then check we are talking to a known firmware"""
        self._serial = serial
        self._serial.write(b'\x55\x55\x00\x00\x00\x00') #Wakeup
        self._cmd(b'\x14\x01\x00\x00') #SAMConfiguration to ensure Wakeup
        if self._cmd(b'\x02') != b'\x03\x32\x01\x06\x07':
            raise Exception('Reader not found')
        
    def _frame(self, data):
        """Construct a 'Normal information frame' based on User Manual section 6.2.1.1"""
        length = len(data) + 1
        lcs = 0x100 - length
        dcs = 0x100 - 0xD4
        for byte in data:
            dcs -= ord(byte)
        dcs &= 0xFF
        return b'\x00\x00\xFF%s%s\xD4%s%s\x00' % (
            chr(length),
            chr(lcs),
            data,
            chr(dcs)
        )

    def _deframe(self, timeout = 1):
        """Read and verify a 'Normal information frame' based on User Manual section 6.2.1.1"""
        prev0 = None
        prev1 = None
        prev2 = None
        start = time.time()
        while timeout == None or timeout > 0:
            self._serial.timeout = timeout
            prev0 = self._serial.read(1)
            if timeout != None:
                timeout -= time.time() - start
            if prev1 == b'\xFF' and prev2 == b'\x00' and not(prev0 ==  b'\x00' or prev0 == b''):
                length = ord(prev0)
                self._serial.timeout = .1
                lcs = ord(self._serial.read(1))
                if 0x100 - length == lcs:
                    buf = self._serial.read(length+2) #data+dcs+postamble
                    if len(buf) == length+2:
                        if buf[0] == b'\xD5':
                            dcs = 0x100
                            for byte in buf:
                                dcs -= ord(byte)
                            dcs &= 0xFF
                            if dcs == 0:
                                #print(' '.join(map(hex,bytearray(buf[1:-2])))) #DEBUG
                                return buf[1:-2]
                continue
            else:
                prev2 = prev1
                prev1 = prev0

    def _cmd(self, data, timeout = 1):
        """Send a command and return the response."""
        self._serial.write(self._frame(data))
        return self._deframe(timeout)

    def auth(self, block, key, key_a = True):
        """Attempt to authenticate a block on current target"""
        return self._cmd(b'\x40%s%s%s%s%s' % (
            self._logical_target,
            b'\x60' if key_a else b'\x61',
            chr(block),
            key,
            self._target
        )) == b'\x41\x00'

    def read(self, block):
        """Read block"""
        buf = self._cmd(b'\x40%s\x30%s' % (
            self._logical_target,
            chr(block),
        ))
        if buf[0:2] == b'\x41\x00':
            return buf[2:]

    def write(self, block, data):
        """Write block"""
        return self._cmd(b'\x40%s\xA0%s%s' % (
            self._logical_target,
            chr(block),
            data
        )) == b'\x41\x00'
   

    def waitfortarget(self):
        """Wait until a target enters the field"""
        while True:
            response = self._cmd(b'\x60\xff\x01\x00', None) #Wait forever
            if response[0] == b'\x61' and response[-5] == b'\04': #Mifare
                self._logical_target = response[-9] #>1 card in field (we use last)
                self._target = response[-4:]
                return self._target

    def unlock(self):
        """Fire the reader's GPIO (to trigger door lock)"""
        self._cmd(b'\x0E\x80\x00')
        time.sleep(.2)
        self._cmd(b'\x0E\x81\x00')
