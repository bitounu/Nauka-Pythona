# Listing_16-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzenie prawid³owo dzia³aj¹cego okna Pygame

import pygame
pygame.init()
ekran = pygame.display.set_mode([640, 480])
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()


