# Listing_17-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rysowanie na ekranie wielu pi³ek z wykorzystaniem sprajtów

import sys, pygame

#-----definicja klasy pochodnej -----------------------------
class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, polozenie):
        pygame.sprite.Sprite.__init__(self)         # wywo³anie inicjalizatora klasy Sprite
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie

#----- g³ówny program -----------------------------
wymiary = szerokosc, wysokosc = 640, 480
ekran = pygame.display.set_mode(wymiary)
ekran.fill([255, 255, 255])
plik_obrazka = "beach_ball.png"
pilki = []
for wiersz in range (0, 3):
    for kolumna in range (0, 3):
        polozenie = [kolumna * 180 + 10, wiersz * 180 + 10]
        pilka = KlasaMojaPilka(plik_obrazka, polozenie)
        pilki.append(pilka)     # dodajemy pi³kê do listy

for pilka in pilki:
    ekran.blit(pilka.image, pilka.rect)
pygame.display.flip()
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
pygame.quit()
