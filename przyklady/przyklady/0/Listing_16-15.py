# Listing_16-15.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odbijanie piłki w dwóch wymiarach

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")
x = 50
y = 50
predkosc_x = 10         # teraz piłka przesuwa się zarówno w osi x
predkosc_y = 10         # jak i y

uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
            
    pygame.time.delay(20)
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    x = x + predkosc_x                          # przesuwamy piłke w poziomie
    y = y + predkosc_y                          # i pionie
    if x > ekran.get_width() - 90 or x < 0:     # odbijamy piłkę od krawędzi bocznych
        predkosc_x = - predkosc_x
    if y > ekran.get_height() - 90 or y < 0:    # odbijamy piłkę od krawędzi górnej i dolnej
        predkosc_y = - predkosc_y

    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()
pygame.quit()

