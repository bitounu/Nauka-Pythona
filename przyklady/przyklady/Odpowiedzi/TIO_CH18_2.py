# TIO_CH18_2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 2, z rozdzia�u 18.

# Program PyPong, w kt�rym pr�dko�� i kierunek poruszania si� pi�ki
# zmienia si� w spos�b losowy

import sys, pygame
import random

class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, predkosc, polozenie):
        pygame.sprite.Sprite.__init__(self)      # wywo�ujemy inicjalizator klasu Sprite 
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc

    def przesun(self):
        global wynik, wynik_czcionka, wynik_powierzchnia
        self.rect = self.rect.move(self.predkosc)
        # odbijamy pi�k� od bocznych kraw�dzi okna
        if self.rect.left < 0 or self.rect.right > ekran.get_width():
            # dodajemy losowo��
            self.predkosc[0] = -self.predkosc[0] + random.randint(-3, 3) 
            self.predkosc[1] = self.predkosc[1] + random.randint(-3, 3)
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > ekran.get_width():  self.rect.right = ekran.get_width()
        

        # odbijamy pi�k� od g�rej i dolnej kraw�dzi okna
        if self.rect.top <= 0 :
            # dodajemy losowo��
            self.predkosc[0] = self.predkosc[0] + random.randint(-3, 3) 
            self.predkosc[1] = -self.predkosc[1] + random.randint(-3, 3)
            self.rect.top = 0
            wynik = wynik + 1

        self.sprawdzPredkosc()    
        wynik_powierzchnia = wynik_czcionka.render(str(wynik), 1, (0, 0, 0))
    
    # sprawdzamy czy w wyniku dobrania losowych warto�ci pr�dko�ci
    # pi�ka nie zacznie przesuwa� si� za szybko    
    def sprawdzPredkosc(self):
        if 0 < mojaPilka.predkosc[0] < 3: mojaPilka.predkosc[0] = 3  
        if -3 < mojaPilka.predkosc[0] <= 0: mojaPilka.predkosc[0] = -3 
        if mojaPilka.predkosc[0] > 15:  mojaPilka.predkosc[0]  = 15
        if 0 < mojaPilka.predkosc[1] < 3: mojaPilka.predkosc[1] = 3  
        if -3 < mojaPilka.predkosc[1] <= 0: mojaPilka.predkosc[1] = -3 
        if mojaPilka.predkosc[1] > 15:  mojaPilka.predkosc[1]  = 15
        
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
mojaPilka = KlasaMojaPilka('wackyball.bmp', [10, 5], [50, 50])
grupaPilka = pygame.sprite.Group(mojaPilka)
paletka = KlasaMojaPaletka([270, 400])
zycia = 3
wynik = 0

wynik_czcionka = pygame.font.Font(None, 50)
wynik_powierzchnia = wynik_czcionka.render(str(wynik), 1, (0, 0, 0))
wynik_polozenie = [10, 10]
koniec = False

uruchomiony = True
while uruchomiony:
    zegar.tick(30)
    ekran.fill([255, 255, 255])
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
        elif zdarzenie.type == pygame.MOUSEMOTION:
            paletka.rect.centerx = zdarzenie.pos[0]
            
    if pygame.sprite.spritecollide(paletka, grupaPilka, False):
        # dodajemy losowo��        
        mojaPilka.predkosc[0] = mojaPilka.predkosc[0] + random.randint(-3, 3) 
        mojaPilka.predkosc[1] = -mojaPilka.predkosc[1] + random.randint(-3, 3)
        mojaPilka.rect.bottom = paletka.rect.top
        
    mojaPilka.przesun()
    
    if not koniec: 
        ekran.blit(mojaPilka.image, mojaPilka.rect)
        ekran.blit(paletka.image, paletka.rect)
        ekran.blit(wynik_powierzchnia, wynik_polozenie)
        for i in range (zycia):
            szerokosc = ekran.get_rect().width
            ekran.blit(mojaPilka.image, [szerokosc - 40 * i, 20])
        pygame.display.flip()
        
    if mojaPilka.rect.top >= ekran.get_rect().bottom:
        # tracimy jedno �ycie, gdy pi�ka wypadnie poza doln� kraw�d� okna
        zycia = zycia - 1
        if zycia == 0:
            koncowy_tekst1 = "Koniec gry"
            koncowy_tekst2 = "Tw�j wynik to: " + str(wynik)
            kt1_czcionka = pygame.font.Font(None, 70)
            kt1_powierzchnia = kt1_czcionka.render(koncowy_tekst1, 1, (0, 0, 0))
            kt2_czcionka = pygame.font.Font(None, 50)
            kt2_powierzchnia = kt2_czcionka.render(koncowy_tekst2, 1, (0, 0, 0))
            ekran.blit(kt1_powierzchnia, [ekran.get_width()/2 - \
                kt1_powierzchnia.get_width()/2, 100])
            ekran.blit(kt2_powierzchnia, [ekran.get_width()/2 - \
                kt2_powierzchnia.get_width()/2, 200])
            pygame.display.flip()
            koniec = True
        else:
            pygame.time.delay(2000) # czekamy 2 sekundy i ponownie wprowadzamy do gry pi�k�
            mojaPilka.rect.topleft = [(ekran.get_rect().width) - 40*zycia, 20]    
pygame.quit()
