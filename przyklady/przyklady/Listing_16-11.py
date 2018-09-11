# Listing_16-11.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pr�bujemy poruszy� pi�k� pla�ow� w oknie Pygame

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")

ekran.blit(moja_pilka, [50, 50])    # rysujemy pi�ke pla�ow�
pygame.display.flip()
pygame.time.delay(2000)             # zatrzymujemy si� na dwie sekundy
ekran.blit(moja_pilka,[150, 50])    # rysujemy pi�k� ponownie

pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

