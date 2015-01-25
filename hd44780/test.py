# -*- coding: utf-8 -*-
#pylint: disable=C0301
"""
>>> import datetime
>>> import time
>>> import hd44780
>>> s = hd44780.Screen()
>>> s.widgets.append(hd44780.Animated(s, hd44780.Coord(0, 1), hd44780.Coord(1, 1), speed = datetime.timedelta(seconds = 1)))
>>> s.widgets[-1].write('|')
>>> s.widgets[-1].write('/')
>>> s.widgets[-1].write('-')
>>> s.widgets.append(hd44780.Animated(s, hd44780.Coord(1, 1), hd44780.Coord(1, 1), speed = datetime.timedelta(seconds = 1)))
>>> s.widgets[-1].write('1')
>>> s.widgets[-1].write('2')
>>> s.widgets[-1].write('3')
>>> s.widgets.append(hd44780.Static(s, hd44780.Coord(1, 0), hd44780.Coord(1, 1)))
>>> s.widgets[-1].write('#')
>>> s.widgets.append(hd44780.TextHScroll(s, hd44780.Coord(2, 0), hd44780.Coord(4, 1), speed = datetime.timedelta(seconds = 1)))
>>> s.widgets[-1].write('abcde µµ ')
>>> s.widgets.append(hd44780.TextHScroll(s, hd44780.Coord(2, 1), hd44780.Coord(4, 1), speed = datetime.timedelta(seconds = 1)))
>>> s.widgets[-1].write('abc')
>>> s.widgets[-1].write('de')
>>> s.widgets.append(hd44780.TextVScroll(s, hd44780.Coord(7, 0), hd44780.Coord(9, 2), speed = datetime.timedelta(seconds = 1)))
>>> s.widgets[-1].write('Testing 123 Wordtoolongfordrisplaybuyalongway testing')
>>> s.render()
>>> s.send()
>>> s.get()
[' #abcd Testing  ', '  abcd 123 Wordt']
>>> time.sleep(1)
>>> s.render()
>>> s.get()
[' #bcde 123 Wordt', '/2bcde oolongfor']
>>> time.sleep(1)
>>> s.get()
[' #bcde 123 Wordt', '/2bcde oolongfor']
>>> s.render()
>>> s.get()
[' #cde  oolongfor', '-3bcde drisplayb']
>>> time.sleep(1)
>>> s.render()
>>> s.get()
[' #de ? drisplayb', '|1bcde uyalongwa']
>>> time.sleep(1)
>>> s.render()
>>> s.get()
[' #e ?? uyalongwa', '/2bcde y testing']
>>> time.sleep(1)
>>> s.render()
>>> s.get()
[' # ??  uyalongwa', '-3bcde y testing']
>>> s.widgets[0].clear()
>>> time.sleep(1)
>>> s.render()
>>> s.get()
[' # ??  uyalongwa', ' 1bcde y testing']
>>> s.widgets[3].remove()
>>> time.sleep(1)
>>> s.render()
>>> s.get()
[' #     uyalongwa', ' 2bcde y testing']
>>> s.put(hd44780.Coord(15,0), 'ab')
Traceback (most recent call last):
Exception: print off screen
>>> s.widgets[0].put(hd44780.Coord(0,0), 'ab')
Traceback (most recent call last):
Exception: print outside of widget
>>> s.widgets.append(hd44780.TextVScroll(s, hd44780.Coord(7, 0), hd44780.Coord(10, 2), speed = datetime.timedelta(seconds = .1)))
Traceback (most recent call last):
Exception: Widget off screen
"""
from __future__ import division, absolute_import, print_function, unicode_literals
