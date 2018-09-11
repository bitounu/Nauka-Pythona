# Listing_16-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# "Sztuka nowoczesna" w kolorze

import pygame, sys, random
from pygame.color import THECOLORS  # skorzystamy z kolorów nazwanych
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
for i in range (100):
    # wybieramy losowe wartoœci dla szerokoœci i wysokoœci prostok¹ta
    szerokosc = random.randint(0, 250); wysokosc = random.randint(0, 100)
    gora = random.randint(0, 400); lewa = random.randint(0, 500)

    # wybieramy losowy kolor
    nazwa_koloru = random.choice(THECOLORS.keys())
    kolor = THECOLORS[nazwa_koloru]

    # wybieramy losow¹ szerkoœæ linii z zakresu od 1 do 3   
    szerokosc_linii = random.randint(1, 3)

    # rysujemy prostok¹t
    pygame.draw.rect(ekran, kolor, [lewa, gora, szerokosc, wysokosc], szerokosc_linii)

pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
