# Listing_19-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Próbujemy odtworzyæ dŸwiêk w Pygame

import pygame, sys
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode([640,480])
pygame.time.delay(1000)     # Czekamy sekundê a¿ mikser siê zainicjalizuje

plask = pygame.mixer.Sound("splat.wav") # Tworzymy obiekt zawieraj¹cy dŸwiêk
plask.play()                            # Odtwarzamy dŸwiêk

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
