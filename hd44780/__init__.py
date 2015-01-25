# -*- coding: utf-8 -*-
"""
HD44780
=======

Simple interface to HD44780 based 16x2 LCD over serial

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    `pylint <../../../cover/hd44780.lint.html>`_,
    `coverage <../../../cover/hd44780___init__.html>`_,
    :doc:`hd44780.test`
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import textwrap
import datetime
import mmap
import serial
import time
import settings

class Coord(object):
    """Simple object for co-ordanetes"""

    def __init__(self, col, row):
        """Setup"""
        self.col = col
        self.row = row

    def contains(self, pos, size):
        """Check if a size and offset fits inside"""
        return pos.col + size.col <= self.col and pos.row + size.row <= self.row

class Screen(object):
    """A colection of Widgets that make up a screen"""

    def __init__(self, size = Coord(16, 2), buf = "screen.dat"):
        "Create buffer"
        self.widgets = []
        self.size = size
        self.lcd = serial.Serial(*settings.HD44780)
        with open(buf, "wb") as screenfile:
            screenfile.truncate()
            screenfile.write(''.ljust(size.row * size.col).encode('ascii'))
        with open(buf, "r+") as screenfile:
            self._buf = mmap.mmap(screenfile.fileno(), 0)
        self.lcd.write('\x1B\x01')

    def render(self):
        """Update the screen"""
        for widget in self.widgets:
            widget.render()

    def send(self):
        """Return bytes to send to display"""
        #NOTE: Could do a lot of optimizing here if needed
        self.lcd.write('\x1B\x02')
        time.sleep(.02)
        for row in range(self.size.row):
            self.lcd.write(self._buf[row * self.size.col:(row + 1) * self.size.col])
            self.lcd.write(b' ' * (40-self.size.col)) 

    def get(self):
        """Return current buffer"""
        buf = []
        for row in range(self.size.row):
            buf.append(self._buf[row * self.size.col:(row + 1) * self.size.col])
        return buf

    def put(self, pos, buf):
        """Output somthing to buffer"""
        if not(self.size.contains(pos, Coord(len(buf), 1))):
            raise Exception("print off screen")
        buf = buf.encode('ascii', 'replace')
        self._buf[pos.row * self.size.col + pos.col:pos.row * self.size.col + pos.col+len(buf)] = buf
    
class Widget(object):
    """Anthing that is displayed on the screen"""

    def __init__(
        self,
        screen,
        pos = Coord(0,0),
        size = Coord(16,1),
        speed = datetime.timedelta(seconds=1)
    ):
        if not(screen.size.contains(pos, size)):
            raise Exception("Widget off screen")        
        self._buf = None
        self._display = None
        self._screen = screen
        self.pos = pos
        self.size = size
        self._speed = speed
        self._nextmove = datetime.datetime.now() + speed

    def write(self, buf):
        """Add content to the widget"""
        if self._buf != None:
            self._buf += buf
        else:
            self._buf = buf

    def clear(self):
        """Clear all content from the widget"""
        self._display = None
        self._buf = None
        for row in range(self.size.row):
            self.put(Coord(0, row), ''.ljust(self.size.col))

    def remove(self):
        """Remove the widget from the screen"""
        self.clear()
        self._screen.widgets.remove(self)

    def put(self, pos, buf):
        """Output somthing to the screen buffer"""
        if not(self.size.contains(pos, Coord(len(buf), 1))):
            raise Exception("print outside of widget")
        pos.row = pos.row + self.pos.row
        pos.col = pos.col + self.pos.col
        self._screen.put(pos, buf)

class TextVScroll(Widget):
    """A textbox where lines of text scroll vertically"""
    
    def __init__(
        self,
        screen,
        pos = Coord(0,0),
        size = Coord(16,2),
        speed = datetime.timedelta(seconds=5)
    ):
        self._lines = []
        super(TextVScroll, self).__init__(screen, pos, size, speed)

    def _popline(self):
        """Move a line from the buffer to the display"""
        self._display.append(self._lines[0])
        self._lines = self._lines[1:]
        self._nextmove = datetime.datetime.now() + self._speed
    
    def render(self):
        """Update display if needed"""
        #Wrap text into line buffers
        if self._display == None:
            self._display = []
        if self._buf != None:
            for line in self._buf.split('\n'):
                self._lines += textwrap.wrap(line, self.size.col)
        self._buf = None
        #Fill display
        while self._lines != [] and len(self._display) < self.size.row:
            self._popline()
        #Scroll (slowly)
        while self._lines != [] and self._nextmove < datetime.datetime.now():
            self._display = self._display[1:]
            self._popline()
        i = 0
        #Rerender if needed
        for line in self._display:
            self.put(
                Coord(0, i),
                line
            )
            i += 1

class TextHScroll(Widget):
    """A textbox were text scrolls horizontally"""
    
    def render(self):
        """Update display if needed"""
        if self._buf != None and len(self._buf) == 0:
            self._buf = None
        if self._buf != None:
            if self._display == None:
                self._display = ''
            #Fill width
            if len(self._display) < self.size.col:
                move = self.size.col - len(self._display)
                self._display += self._buf[:move]
                self._buf = self._buf[move:]
            #Scroll
            if self._nextmove < datetime.datetime.now():
                self._display = self._display[1:]
                self._display += self._buf[0]
                self._buf = self._buf[1:]
                self._nextmove = datetime.datetime.now() + self._speed
            self.put(Coord(0, 0), self._display)

class Static(Widget):
    """Simplest posible Widget"""

    def render(self):
        """Update display if needed"""
        if self._buf != None:
            display = self._buf[:self.size.col]
            self._buf = None
            self.put(Coord(0, 0), display)

class Animated(Static):
    """Cycle betweem diffrent display"""

    def __init__(
        self,
        screen,
        pos = Coord(0,0),
        size = Coord(1, 1),
        speed = datetime.timedelta(seconds=1)
    ):
        self._bufs = []
        self._current = 0
        super(Animated, self).__init__(screen, pos, size, speed)

    
    def write(self, buf):
        """Add content to the widget"""
        self._bufs.append(buf)

    def clear(self):
        """Clear all content from the widget"""
        super(Animated, self).clear()
        self._bufs = []

    def render(self):
        """Update display if needed"""
        if self._bufs != []:
            if self._nextmove < datetime.datetime.now():
                self._current += 1
                self._current %= len(self._bufs)
                self._buf = self._bufs[self._current]
                self._nextmove = datetime.datetime.now() + self._speed
                super(Animated, self).render()
