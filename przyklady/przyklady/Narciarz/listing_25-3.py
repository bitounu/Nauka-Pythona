# Listing 25-3
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# £¹czymy ze sob¹ narciarza i przeszkody, ale nie implementujemy jeszcze wykrywania zderzeñ

import pygame, sys, random

# W zale¿noœci od kierunku, w którym porusza siê narciarz, wyœwietlamy inny rysunek
narciarz_rysunki = ["skier_down.png", "skier_right1.png",
                "skier_right2.png", "skier_left2.png",
                "skier_left1.png"]

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

# Klasa zawieraj¹ca sprajt z przeszkod¹ (z drzewkiem lub flag¹)
class KlasaPrzeszkoda(pygame.sprite.Sprite):
    def __init__(self, plik_graficzny, pole, rodzaj):
        pygame.sprite.Sprite.__init__(self)
        self.plik_graficzny = plik_graficzny
        self.image = pygame.image.load(plik_graficzny)
        self.rect = self.image.get_rect()
        self.rect.center = pole
        self.rodzaj = rodzaj
        self.zaliczona = False

    def update(self):
        global predkosc
        self.rect.centery -= predkosc[1]
        if self.rect.centery < -32:
            self.kill()

# Tworzymy „ekran” wype³niony przeszkodami
# Korzystamy z bloków o rozmiarach 64 x 64 pikseli tak, aby przeszkody nie znajdowa³y siê zbyt blisko siebie
def utworz_mape():
    global przeszkody
    zajete_pola = []
    for i in range(10):     # Na ekranie umieszczamy 10 przeszkód
        wiersz = random.randint(0, 9)
        kolumna = random.randint(0, 9)
        pole = [kolumna * 64 + 20, wiersz * 64 + 20 + 640] # Wspó³rzêdne z i y œrodka przeszkody
        if not (pole in zajete_pola):           # # Nie dopuszczamy do umieszczenia dwóch przeszkód w jednym miejscu
            zajete_pola.append(pole)
            rodzaj = random.choice(["drzewko", "flaga"])
            if rodzaj == "drzewko": rysunek = "skier_tree.png"
            elif rodzaj == "flaga": rysunek = "skier_flag.png"
            przeszkoda = KlasaPrzeszkoda(rysunek, pole, rodzaj)
            przeszkody.add(przeszkoda)

# Odmalowujemy ekran, ³¹cznie z wszystkimi sprajtami
def animuj():
    ekran.fill([255, 255, 255])
    przeszkody.draw(ekran)
    ekran.blit(narciarz.image, narciarz.rect)    
    pygame.display.flip()

# Inicjalizacja
pygame.init()
ekran = pygame.display.set_mode([640,640])
zegar = pygame.time.Clock()
punkty = 0
predkosc = [0, 6]
narciarz = KlasaNarciarz()
przeszkody = pygame.sprite.Group() # hrupa zawieraj¹ca obiekty przeszkód
pozycja_mapy = 0
utworz_mape()       # Tworzymy ekran wype³niony przeszkodami

# G³ówna pêtla zdarzeñ Pygame
uruchomiona = True
while uruchomiona:
    zegar.tick(30)
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False

        if zdarzenie.type == pygame.KEYDOWN:  # Sprawdzamy, czy zosta³ naciœniêty klawisz
            if zdarzenie.key == pygame.K_LEFT:  # Klawisz ze strza³k¹ w lewo obraca narciarza w lewo
                predkosc = narciarz.obroc(-1)
            elif zdarzenie.key == pygame.K_RIGHT:   # Klawisz ze strza³k¹ w prawo obraca narciarza w prawo
                predkosc = narciarz.obroc(1)
    narciarz.przesun(predkosc)      # Przesuwany marciarza (w lewo i w prawo)
    pozycja_mapy += predkosc[1]     # Przewijamy ekran z przeszkodami

    # Poni¿ej okna tworzymy nowy ekran z przeszkodami 
    if pozycja_mapy >=640:
        utworz_mape()
        pozycja_mapy = 0

    przeszkody.update()   
    animuj()

pygame.quit()

    
