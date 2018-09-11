# Listing_19-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Oczekiwanie na koniec piosenki

import pygame, sys
pygame.init()
pygame.mixer.init()

ekran = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()
plask = pygame.mixer.Sound("splat.wav")
plask.set_volume(0.50)

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
            
    if not pygame.mixer.music.get_busy():   # Sprawdzamy czy piosenka siê ju¿ skoñczy³a
        plask.play()                        # Odtwarzamy dŸwiêk
        pygame.time.delay(1000)             # Czekamy sekundê a¿ skoñczy siê dŸwiêk "plaœniêcia"
        uruchomiony = False
        
pygame.quit()

