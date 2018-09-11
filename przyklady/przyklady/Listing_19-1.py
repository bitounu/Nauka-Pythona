# Listing_19-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pr�bujemy odtworzy� d�wi�k w Pygame

import pygame, sys
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode([640,480])
pygame.time.delay(1000)     # Czekamy sekund� a� mikser si� zainicjalizuje

plask = pygame.mixer.Sound("splat.wav") # Tworzymy obiekt zawieraj�cy d�wi�k
plask.play()                            # Odtwarzamy d�wi�k

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
