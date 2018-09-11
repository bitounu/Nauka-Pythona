# Listing_16-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzymy "sztuk� nowoczesn�" rysuj�c w spos�b losowy prostok�ty

import pygame, sys, random
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])

# rysujemy 100 prostok�t�w
for i in range (100):
    # wybieramy losowe warto�ci dla szeroko�ci i wysoko�ci prostok�ta
    szerokosc = random.randint(0, 250)
    wysokosc = random.randint(0, 100)
    gora = random.randint(0, 400)
    lewa = random.randint(0, 500)

    # rysujemy prostok�t
    pygame.draw.rect(ekran, [0,0,0], [lewa, gora, szerokosc, wysokosc], 1)
    
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

