# Listing 25-2
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzymy grê Narciarz — fragment odpowiedzialny za animacjê przeszkód

import pygame, sys, random

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

# Tworzymy „ekran” wype³niony przeszkodami
# Korzystamy z bloków o rozmiarach 64 x 64 pikseli tak, aby przeszkody nie znajdowa³y siê zbyt blisko siebie
def utworz_mape():
    global przeszkody
    zajete_pola = []
    for i in range(10):     # Na ekranie umieszczamy 10 przeszkód
        wiersz = random.randint(0, 9)
        kolumna = random.randint(0, 9)
        pole = [kolumna * 64 + 20, wiersz * 64 + 20 + 640]  # Wspó³rzêdne z i y œrodka przeszkody
        if not (pole in zajete_pola):           # Nie dopuszczamy do umieszczenia dwóch przeszkód w jednym miejscu
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
    pygame.display.flip()

# Inicjalizacja
pygame.init()
ekran = pygame.display.set_mode([640,640])
zegar = pygame.time.Clock()
predkosc = [0, 6]
przeszkody = pygame.sprite.Group()
pozycja_mapy = 0
utworz_mape()

# G³ówna pêtla zdarzeñ Pygame
uruchomiona = True
while uruchomiona:
    zegar.tick(30)
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False

    pozycja_mapy += predkosc[1]     # Przewijamy ekran z przeszkodami

    # Poni¿ej okna tworzymy nowy ekran z przeszkodami 
    if pozycja_mapy >=640:
        utworz_mape()
        pozycja_mapy = 0

    przeszkody.update()   
    animuj()

pygame.quit()

    
