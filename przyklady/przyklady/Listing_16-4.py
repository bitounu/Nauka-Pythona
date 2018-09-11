# Listing_16-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rysowanie okrêgu na œrodku okna

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255,255,255])

# rysujemy okr¹g w samym œrodku okna Pygame
pygame.draw.circle(ekran, [255,0,0],[320,240], 30, 0)   # nowe po³o¿enie okrêgu to [320,240]
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
