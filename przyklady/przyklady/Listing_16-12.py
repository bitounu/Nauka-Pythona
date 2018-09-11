# Listing_16-12.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Ponownie próbujemy poruszyæ pi³k¹ w oknie Pygame

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")
ekran.blit(moja_pilka, [50, 50])                # rysujemy pi³kê
pygame.display.flip()
pygame.time.delay(2000)
ekran.blit(moja_pilka,[150, 50])                # rysujemy pi³kê w innym miejscu

# "wymazujemy" obrazek pierwszej pi³ki
pygame.draw.rect(ekran, [255,255,255], [50, 50, 90, 90], 0)

pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

