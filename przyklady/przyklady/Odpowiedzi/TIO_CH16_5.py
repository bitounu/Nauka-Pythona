# TIO_CH16-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 5, z rozdzia³u 16.

# Umieœæ wywo³eni funkcji display.flip wewn¹trz pêtli while
# i wprowadŸ opóŸnienie

import pygame, sys, random
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
for i in range (100):
    szerokosc = random.randint(0, 250)
    wysokosc = random.randint(0, 100)
    gora = random.randint(0, 400)
    lewa = random.randint(0, 500)
    pygame.draw.rect(ekran, [0,0,0], [lewa, gora, szerokosc, wysokosc], 1)
    pygame.display.flip()
    pygame.time.delay(30)
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
