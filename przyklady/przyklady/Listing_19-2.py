# Listing_19-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odtwarzamy muzykê

import pygame, sys

pygame.init()
pygame.mixer.init()

ekran = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("bg_music.mp3")     # £adujemy plik muzyczny
pygame.mixer.music.play()                   # Odtwarzamy muzykê

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
