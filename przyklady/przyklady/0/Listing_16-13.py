# Listing_16-13.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Płynne przemieszczanie obrazka piłki plażowej

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")

# rozpoczynamy w położeniu [50,50]
x = 50
y = 50
ekran.blit(moja_pilka, [50, 50])
pygame.display.flip()
for petla in range (1, 100):
    pygame.time.delay(20)

    # wymazujemy piłkę w poprzednim położeniu, zamalowując ją białym kolorem      
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    
    # przesuwamy piłkę w poziomie, zmieniając jej współrzędną x 
    x = x + 5

    # rysujemy piłke w nowym położeniu
    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()

uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

