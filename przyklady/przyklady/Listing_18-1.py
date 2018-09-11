# Listing_18-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Program z odbijaj¹c¹ siê pi³k¹, sprajtami i funkcj¹ clock.tick()

import pygame, sys
pygame.init()
ekran = pygame.display.set_mode([640,480])
tlo = pygame.Surface(ekran.get_size())
tlo.fill([255, 255, 255])
zegar = pygame.time.Clock()

# Klasa Pilka zawieraj¹ca metodê przesun()
class Pilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, predkosc, polozenie):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc
        
    def przesun(self):
        if self.rect.left <= ekran.get_rect().left or \
                self.rect.right >= ekran.get_rect().right:
            self.predkosc[0] = - self.predkosc[0]
        nowaPozycja = self.rect.move(self.predkosc)
        self.rect = nowaPozycja

# Tworzymy instancjê pi³ki
moja_pilka = Pilka('beach_ball.png', [10,0], [20, 20])

uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False
            
    zegar.tick(30)
    ekran.blit(tlo, (0, 0))
    moja_pilka.przesun()
    ekran.blit(moja_pilka.image, moja_pilka.rect)
    pygame.display.flip()
pygame.quit()
