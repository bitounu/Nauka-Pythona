# Listing_16-13.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# P³ynne przemieszczanie obrazka pi³ki pla¿owej

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
ekran.fill([255, 255, 255])
moja_pilka = pygame.image.load("beach_ball.png")

# rozpoczynamy w po³o¿eniu [50,50]
x = 50
y = 50
ekran.blit(moja_pilka, [50, 50])
pygame.display.flip()
for petla in range (1, 100):
    pygame.time.delay(20)

    # wymazujemy pi³kê w poprzednim po³o¿eniu, zamalowuj¹c j¹ bia³ym kolorem      
    pygame.draw.rect(ekran, [255,255,255], [x, y, 90, 90], 0)
    
    # przesuwamy pi³kê w poziomie, zmieniaj¹c jej wspó³rzêdn¹ x 
    x = x + 5

    # rysujemy pi³ke w nowym po³o¿eniu
    ekran.blit(moja_pilka, [x, y])
    pygame.display.flip()

uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()

