# Listing_16-14.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odbijanie pi³ki pla¿owej w oknie Pygame

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")
x = 50
y = 50

predkosc_x = 10             # z taka prêdkoœci¹ bêdzie sie przesuwa³a pi³ka                                    
                            # o 10 pikseli w ka¿dej iteracji pêtli
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False

    pygame.time.delay(20)
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    x = x + predkosc_x                      # przesuwamy pi³kê
    if x > ekran.get_width() - 90 or x < 0: # sprawdzamy czy nastapi³o zderzenie z krawêdzi¹ okna
        predkosc_x = - predkosc_x           # odwracamy kierunek ruchu pi³ki
    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()
pygame.quit()

