# listing_25-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzymy grê Narciarz — fragment odpowiedzialny za animacjê narciarza

import pygame, sys, random

# W zale¿noœci od kierunku, w którym porusza siê narciarz, wyœwietlamy inny rysunek
narciarz_rysunki = ["skier_down.png", "skier_right1.png",
                "skier_right2.png", "skier_left2.png",
                "skier_left1.png"]

# Klasa sprajta narciarza
class KlasaNarciarz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.nachylenie = 0

    def obroc(self, kierunek):
        # Gdy narciarz siê obraca, ³adujemy nowy obrazek i zmieniamy prêdkoœæ
        self.nachylenie = self.nachylenie + kierunek
        if self.nachylenie < -2: self.nachylenie = -2
        if self.nachylenie > 2: self.nachylenie = 2
        srodek = self.rect.center
        self.image = pygame.image.load(narciarz_rysunki[self.nachylenie])
        self.rect = self.image.get_rect()
        self.rect.center = srodek
        predkosc = [self.nachylenie, 6 - abs(self.nachylenie) * 2]
        return predkosc

    def przesun(self, predkosc):
        # Przesuwamy narciarza w prawo i w lewo
        self.rect.centerx = self.rect.centerx + predkosc[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

# Odmalowujemy ekran, ³¹cznie z wszystkimi sprajtami
def animuj():
    ekran.fill([255, 255, 255])
    ekran.blit(narciarz.image, narciarz.rect)    
    pygame.display.flip()

# Inicjalizacja
pygame.init()
ekran = pygame.display.set_mode([640,640])
zegar = pygame.time.Clock()
narciarz = KlasaNarciarz()
predkosc = [0, 6]

# G³ówna pêtla zdarzeñ Pygame
uruchomiona = True
while uruchomiona:
    zegar.tick(30)
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False
        if zdarzenie.type == pygame.KEYDOWN:    # Sprawdzamy, czy zosta³ naciœniêty klawisz
            if zdarzenie.key == pygame.K_LEFT:  # Klawisz ze strza³k¹ w lewo obraca narciarza w lewo
                predkosc = narciarz.obroc(-1)
            elif zdarzenie.key == pygame.K_RIGHT:   # Klawisz ze strza³k¹ w prawo obraca narciarza w prawo
                predkosc = narciarz.obroc(1)
    narciarz.przesun(predkosc)
    animuj()
pygame.quit()

    
