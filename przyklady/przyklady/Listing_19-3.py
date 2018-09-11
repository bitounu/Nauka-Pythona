# Listing_19-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Sterowanie g³oœnoœci¹ dŸwiêków i muzyki

import pygame, sys
pygame.init()
pygame.mixer.init()

ekran = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.30)     # Zmieniamy g³oœnoœæ muzyki
pygame.mixer.music.play()
plask = pygame.mixer.Sound("splat.wav") # Zmieniamy g³oœnoœæ efektu "plaœniêcia"
plask.set_volume(0.50)
plask.play()

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
