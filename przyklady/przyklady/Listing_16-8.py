# Listing_16-8.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Ci�g�a fala sinusoidalna

import pygame, sys
import math
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
punktyWykresu = []
for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)    # wz�r na fal� sinusoidaln�
    punktyWykresu.append([x, y])                            # tworzymy list� punkt�w
    
pygame.draw.lines(ekran, [0,0,0],False, punktyWykresu, 1)   # rysujemy punkty, ��cz�c je ze sob� prostymi

pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
