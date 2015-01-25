# -*- coding: utf-8 -*-
"""
Status Display
==============

Provide a simple graphical display using pygame on the framebuffer.

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    `pylint <../../../cover/status.lint.html>`_,
    `coverage <../../../cover/status___init__.html>`_,
    :doc:`status.test`
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import os
import pygame
import time
import math
import datetime

def _offset(pos, radius, angle):
    return (pos[0] + math.sin(angle) * radius, pos[1] + math.cos(angle) * radius)

def _gethour():
    return -math.pi/2 - math.pi * 2 / 12 * ((time.time() - time.daylight * time.altzone) % (60*60*12) / 60 / 60)

def _getmin():
    return -math.pi/2 - math.pi * 2 / 60 * ((time.time() - time.daylight * time.altzone) % (60*60*12) / 60 ) % 60

def _getsec():
    return -math.pi/2 - math.pi * 2 / 60 * ((time.time() - time.daylight * time.altzone) % (60*60*12)) % (60 * 60)

class Status(object):
    screen = None;
    
    def __init__(self):
        if not os.getenv('SDL_VIDEODRIVER'):
            os.putenv('SDL_VIDEODRIVER', 'fbcon')
        pygame.display.init()
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        pygame.font.init()

    def run(self):
        clock = pygame.Surface(self.screen.get_size())
        clock = clock.convert()      
        clockpos = (self.screen.get_rect().centerx, self.screen.get_rect().centery)

        font = pygame.font.Font(pygame.font.match_font('freemono', True), 72)
        text = font.render('Hello World', True, (255, 128, 128))
        text = pygame.transform.rotate(text, 90)
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        textpos.centery = self.screen.get_rect().centery

        dir = 2
        while True:
            start = time.time()

            self.screen.fill((0, 0, 0))
            pygame.draw.line(self.screen, (0, 0, 100), clockpos, _offset(clockpos, 500, _gethour()), 20)
            pygame.draw.line(self.screen, (0, 0, 200), clockpos, _offset(clockpos, 500, _getmin()), 10)
            pygame.draw.line(self.screen, (0, 0, 255), clockpos, _offset(clockpos, 500, _getsec()), 2)
            
            textpos.centerx += dir
            if textpos.centerx > self.screen.get_size()[0] or textpos.centerx < 0:
                dir = -dir
            self.screen.blit(text, textpos)

            pygame.display.flip()
            try:
                time.sleep(.1/25-(time.time()-start))
            except:
                pass

