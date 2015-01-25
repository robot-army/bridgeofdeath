# -*- coding: utf-8 -*-
"""
Sonmicro SM130 RFID Mifare® read/write module.
"""
from __future__ import division, absolute_import, print_function, unicode_literals
import time
import serial

class SM130(object):
    """
    Sonmicro SM130 RFID Mifare® read/write module.
    """
    _target = None

    def __init__(self, serial):
        """Check we are talking to a known firmware."""
        self._serial = serial
        if self._cmd(b'\x80') != b'\x81UM 1.3d':
            raise Exception('Reader not found')

    def _frame(self, data):
        """Construct a 'UART frame' based on Data Sheet section 4.1."""
        length = len(data)
        csum = length
        for byte in data:
            csum += ord(byte)
        csum &= 0xFF
        return b'\xFF\x00%s%s%s' % (
            chr(length),
            data,
            chr(csum)
        )

    def _deframe(self, timeout):
        """Read and verify a 'UART frame' based on Data Sheet section 4.1."""
        prev0 = None
        prev1 = None
        prev2 = None
        start = time.time()
        while timeout == None or timeout > 0:
            self._serial.timeout = timeout
            prev0 = self._serial.read(1)
            if timeout != None:
                timeout -= time.time() - start
            if prev1 == b'\x00' and prev2 == b'\xFF' and not(prev0 ==  b'\x00' or prev0 == b''):
                length = ord(prev0)
                self._serial.timeout = 1
                buf = self._serial.read(length + 1) #data+csum
                if len(buf) == length + 1:
                    csum = length
                    for byte in buf[:-1]:
                        csum += ord(byte)
                    csum &= 0xFF
                    if csum == ord(buf[-1]):
                        return buf[:-1]
                continue
            else:
                prev2 = prev1
                prev1 = prev0

    def _cmd(self, data, timeout = 2):
        """Send a command and return the response."""
        self._serial.write(self._frame(data))
        return self._deframe(timeout)

    def auth(self, block, key, key_a = True):
        """Attempt to authenticate a block on current target"""
        return self._cmd(b'\x85%s%s%s' % (
            chr(block),
            b'\xAA' if key_a else b'\xBB',
            key
        )) == b'\x85L'

    def read(self, block):
        """Read block"""
        buf = self._cmd(b'\x86%s' % (
            chr(block),
        ))
        if buf[0] == b'\x86' and ord(buf[1]) == block:
            return buf[2:]

    def write(self, block, data):
        """Write block"""
        cmd = b'\x89%s%s' % (
            chr(block),
            data
        )
        buf = self._cmd(cmd)
        return buf == cmd or buf == b'\x89\x58' or buf == b'\x89\x55'

    def waitfortarget(self):
        """Wait until a target enters the field"""
        while True:
            response = self._cmd(b'\x82')
            if response == b'\x82L': #cmd in progress
                response = self._deframe(None) #Wait forever
                if response[0:2] == b'\x82\x02': #Mifare 1k
                    self._target = response[-4:]
                    return self._target            

    def unlock(self):
        ss = serial.Serial('/dev/ttyACM0',115200)
        ss.write('\x05')
        #self._cmd(b'\x92\x03')
        #time.sleep(.2)
        #self._cmd(b'\x92\x00')
