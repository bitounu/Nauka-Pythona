# Listing_16-14.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odbijanie piłki plażowej w oknie Pygame

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")
x = 50
y = 50

predkosc_x = 10             # z taka prędkością będzie sie przesuwała piłka                                    
                            # o 10 pikseli w każdej iteracji pętli
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False

    pygame.time.delay(20)
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    x = x + predkosc_x                      # przesuwamy piłkę
    if x > ekran.get_width() - 90 or x < 0: # sprawdzamy czy nastapiło zderzenie z krawędzią okna
        predkosc_x = - predkosc_x           # odwracamy kierunek ruchu piłki
    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()
pygame.quit()

