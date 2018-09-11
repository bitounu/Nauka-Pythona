# Listing_16-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rysowanie linii za pomoc¹ wielu ma³ych prostok¹tów

import pygame, sys
import math
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])

for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)    # wzór na falê sinusoidaln¹

    # rysujemy poszczególne punkty jako ma³e prostok¹ty
    pygame.draw.rect(ekran, [0,0,0],[x, y, 1, 1], 1) # wspó³rzêdne x i y okreœlaj¹ po³o¿enie ka¿dego prostok¹ta
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

