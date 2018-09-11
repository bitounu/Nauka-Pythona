# Listing_16-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rysowanie linii za pomocą wielu małych prostokątów

import pygame, sys
import math
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])

for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)    # wzór na falę sinusoidalną

    # rysujemy poszczególne punkty jako małe prostokąty
    pygame.draw.rect(ekran, [0,0,0],[x, y, 1, 1], 1) # współrzędne x i y określają położenie każdego prostokąta
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

