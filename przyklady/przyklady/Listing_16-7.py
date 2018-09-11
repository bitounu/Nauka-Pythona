# Listing_16-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rysowanie linii za pomoc� wielu ma�ych prostok�t�w

import pygame, sys
import math
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])

for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)    # wz�r na fal� sinusoidaln�

    # rysujemy poszczeg�lne punkty jako ma�e prostok�ty
    pygame.draw.rect(ekran, [0,0,0],[x, y, 1, 1], 1) # wsp�rz�dne x i y okre�laj� po�o�enie ka�dego prostok�ta
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

