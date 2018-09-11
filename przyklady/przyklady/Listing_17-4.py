# Listing_17-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z klasy Clock() i funkcji get_fps()

import sys, pygame
from random import *

class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, polozenie, predkosc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc
    def przesun(self):
        self.rect = self.rect.move(self.predkosc)
        # sprawdzamy, czy pi³ka uderzy³a w boczn¹ krawêdŸ okna
        # je¿eli tak, odwracamy kierunek ruchu pi³ki w osi x
        if self.rect.left < 0 or self.rect.right > szerokosc:
            self.predkosc[0] = -self.predkosc[0]
        # sprawdzamy, czy pi³ka uderzy³a w górn¹ b¹dŸ doln¹ krawêdŸ okna
        # je¿eli tak, odwracamy kierunek ruchu pi³ki w osi y  
        if self.rect.top < 0 or self.rect.bottom > wysokosc:
            self.predkosc[1] = -self.predkosc[1]

def animuj(grupa):
    ekran.fill([255,255,255])
    for pilka in grupa:
        pilka.przesun()
    for pilka in grupa:
        # usuwamy sprajta z grupy
        grupa.remove(pilka)

        # sprawdzamy, czy nie nast¹pi³o zderzenie sprajta z pozosta³ymi sprajtami z grupy
        if pygame.sprite.spritecollide(pilka, grupa, False):
            pilka.predkosc[0] = -pilka.predkosc[0]
            pilka.predkosc [1] = -pilka.predkosc [1]

        # wstawiamy z powrotem pi³kê do grupy    
        grupa.add(pilka)        
        ekran.blit(pilka.image, pilka.rect)
    pygame.display.flip()
    
#----- g³ówny program -----------------------------
rozmiar = szerokosc, wysokosc = 640, 480
ekran = pygame.display.set_mode(rozmiar)
ekran.fill([255, 255, 255])
plik_obrazka = "beach_ball.png"
zegar = pygame.time.Clock()
grupa = pygame.sprite.Group()
for wiersz in range (0, 2):
    for kolumna in range (0, 2):
        polozenie = [kolumna * 180 + 10, wiersz * 180 + 10]
        predkosc = [choice([-2, 2]), choice([-2, 2])]
        pilka = KlasaMojaPilka(plik_obrazka, polozenie, predkosc)
        grupa.add(pilka)    # dodajemy pi³kê do grupy

uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
            liczba_klatek = zegar.get_fps()
            print "liczba klatek = ", liczba_klatek
    animuj(grupa)
    zegar.tick(30)
pygame.quit()

