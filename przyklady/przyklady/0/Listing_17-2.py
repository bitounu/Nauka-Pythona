# Listing 17-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Program służący do poruszania piłkami za pomocą sprajtów

import sys, pygame
from random import *

#-----definicja klasy pochodnej -----------------------------
class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, polozenie, predkosc):
        pygame.sprite.Sprite.__init__(self)  # wywołanie inicjalizatora klasy Sprite
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc

    def przesun(self):
        self.rect = self.rect.move(self.predkosc)
        # sprawdzamy, czy piłka uderzyła w boczną krawędź okna
        # jeżeli tak, odwracamy kierunek ruchu piłki w osi x
        if self.rect.left < 0 or self.rect.right > szerokosc:
            self.predkosc[0] = -self.predkosc[0]
        # sprawdzamy, czy piłka uderzyła w górną bądź dolną krawędź okna
        # jeżeli tak, odwracamy kierunek ruchu piłki w osi y
        if self.rect.top < 0 or self.rect.bottom > wysokosc:
            self.predkosc[1] = -self.predkosc[1]

#----- główny program -----------------------------
rozmiar = szerokosc, wysokosc = 640, 480
ekran = pygame.display.set_mode(rozmiar)
ekran.fill([255, 255, 255])
plik_obrazka = "beach_ball.png"
pilki = []
for wiersz in range (0, 3):
    for kolumna in range (0, 3):
        polozenie = [kolumna * 180 + 10, wiersz * 180 + 10]
        predkosc = [choice([-2, 2]), choice([-2, 2])]
        pilka = KlasaMojaPilka(plik_obrazka, polozenie, predkosc)
        pilki.append(pilka)  # dodajemy piłkę do listy
        
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
    pygame.time.delay(20)
    ekran.fill([255, 255, 255])
    for pilka in pilki:
        pilka.przesun()
        ekran.blit(pilka.image, pilka.rect)
    pygame.display.flip()
pygame.quit()

