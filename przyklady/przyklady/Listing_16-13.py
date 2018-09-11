# Listing_16-13.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# P�ynne przemieszczanie obrazka pi�ki pla�owej

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")

# rozpoczynamy w po�o�eniu [50,50]
x = 50
y = 50
ekran.blit(moja_pilka, [50, 50])
pygame.display.flip()
for petla in range (1, 100):
    pygame.time.delay(20)

    # wymazujemy pi�k� w poprzednim po�o�eniu, zamalowuj�c j� bia�ym kolorem      
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    
    # przesuwamy pi�k� w poziomie, zmieniaj�c jej wsp�rz�dn� x 
    x = x + 5

    # rysujemy pi�ke w nowym po�o�eniu
    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()

uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

