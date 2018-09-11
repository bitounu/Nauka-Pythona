# Listing_18-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pierwsza wersja PyPonga

import sys, pygame
from pygame.locals import *

# definicja klasy pi�ki
class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, predkosc, polozenie):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc

    def przesun(self):
        self.rect = self.rect.move(self.predkosc)
        # odbijamy pi�k� od bocznych kraw�dzi okna
        if self.rect.left < 0 or self.rect.right > ekran.get_width():
            self.predkosc[0] = -self.predkosc[0]

        # odbijamy pi�k� od g�rej i dolnej kraw�dzi okna
        if self.rect.top <= 0: 
            self.predkosc[1] = -self.predkosc[1]

# definicja klasy paletki
class KlasaMojaPaletka(pygame.sprite.Sprite):
    def __init__(self, polozenie):
        pygame.sprite.Sprite.__init__(self)
        obrazek_powierzchnia = pygame.surface.Surface([100, 20])
        obrazek_powierzchnia.fill([0,0,0])
        self.image = obrazek_powierzchnia.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie

pygame.init()
ekran = pygame.display.set_mode([640,480])
zegar = pygame.time.Clock()
predkosc_pilki = [10, 5]
mojaPilka = KlasaMojaPilka('wackyball.bmp', predkosc_pilki, [50, 50]) # tworzymy instancje pi�ki 
grupaPilka = pygame.sprite.Group(mojaPilka) # dodajemy pi�k� do grupy sprajt�w
paletka = KlasaMojaPaletka([270, 400])      # tworzymy instancj� paletki

uruchomiony = True
while uruchomiony:
    zegar.tick(30)
    ekran.fill([255, 255, 255])
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
        elif zdarzenie.type == pygame.MOUSEMOTION:  # przesuwamy paletk�
            paletka.rect.centerx = zdarzenie.pos[0] # w momencie poruszenia mysz�

    if pygame.sprite.spritecollide(paletka, grupaPilka, False): # odbijamy pi�k� 
        mojaPilka.predkosc[1] = -mojaPilka.predkosc[1]          # gdy uderzy ona w paletk�
    mojaPilka.przesun()    
    ekran.blit(mojaPilka.image, mojaPilka.rect)
    ekran.blit(paletka.image, paletka.rect)    
    pygame.display.flip()
pygame.quit()

