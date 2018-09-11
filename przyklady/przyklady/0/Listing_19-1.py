# Listing_19-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Próbujemy odtworzyć dźwięk w Pygame

import pygame, sys
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode([640,480])
pygame.time.delay(1000)     # Czekamy sekundę aż mikser się zainicjalizuje

plask = pygame.mixer.Sound("splat.wav") # Tworzymy obiekt zawierający dźwięk
plask.play()                            # Odtwarzamy dźwięk

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
