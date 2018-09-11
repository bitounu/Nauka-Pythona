# Listing_16-16.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Poruszanie pi³k¹ z zawijaniem

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")
x = 50
y = 50
predkosc_x = 5

uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
    pygame.time.delay(20)
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    x = x + predkosc_x
    if x > ekran.get_width():   # je¿eli pi³ka zniknie po prawej stronie okna
        x = 0                   # pojawi siê ponownie z lewej strony okna
    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()
pygame.quit()


