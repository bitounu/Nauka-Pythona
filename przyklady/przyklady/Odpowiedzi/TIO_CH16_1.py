# TIO_CH16_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowiedü do zadania praktycznego 1, z rozdzia≥u 16.

import pygame, sys
pygame.init()
ekran=pygame.display.set_mode((640, 480))
ekran.fill((250, 120, 0))
pygame.draw.arc(ekran, (255, 255, 0), pygame.rect.Rect(43, 368, 277, 235),
   -6.25, 0, 15)
pygame.draw.rect(ekran, (255, 0, 0), pygame.rect.Rect(334, 191, 190, 290))
pygame.draw.rect(ekran, (128, 64, 0), pygame.rect.Rect(391, 349, 76, 132))
pygame.draw.line(ekran, (0, 255, 0), (268, 259), (438, 84), 25)
pygame.draw.line(ekran, (0, 255, 0), (578, 259), (438, 84), 25)
pygame.draw.circle(ekran, (0, 0, 0), (452, 409), 11, 2)
pygame.draw.polygon(ekran, (0, 0, 255), [(39, 39), (44, 136), (59, 136),
   (60, 102), (92, 102), (94, 131), (107, 141), (111, 50), (97, 50), (93,
   86), (60, 82), (58, 38)], 5)
pygame.draw.rect(ekran, (0, 0, 255), pygame.rect.Rect(143, 90, 23, 63), 5)
pygame.draw.circle(ekran, (0, 0, 255), (153, 60), 15, 5)
zegar = pygame.time.Clock()
pygame.display.flip()

uruchomiony = True
while uruchomiony:
    clock.tick(60)
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
        elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_ESCAPE:
            uruchomiony = False
pygame.quit()
