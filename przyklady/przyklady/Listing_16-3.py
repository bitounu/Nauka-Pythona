# Listing_16-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Drawing a circle

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255,255,255])                               # wype³niamy okno bia³ym t³em
pygame.draw.circle(ekran, [255,0,0],[100,100], 30, 0)   # rysujemy okr¹g
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
