# Listing_10-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Narciarz

import pygame, sys, random
# osobny obrazek dla ka¿dego mo¿liwego ruchu narciarza
narciarz_rysunki = ["skier_down.png", "skier_right1.png",
                "skier_right2.png", "skier_left2.png",
                "skier_left1.png"]

# klasa sprajtu narciarza
class KlasaNarciarz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.nachylenie = 0

    def obroc(self, kierunek):
        # gdy narciaz skrêca, ³adujemy nowy obrazek i zmieniamy prêdkoœc 
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
        # przesuwamy narciarza w lewo i w prawo
        self.rect.centerx = self.rect.centerx + predkosc[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

# klasa sprajtu przeszkody (drzewka i flagi)
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

# tworzymy ekran zawieraj¹cy przeszkody o rozdzielczoœci 640 x 640
# ekran dzielimy na bloki o rozmiarach 64 x 64 pikseli tak, aby obiekty nie znajdowa³y siê zbyt blisko siebie
def utworz_mape():
    global przeszkody
    zajete_pola = []
    for i in range(10):                  # 10 przeszkód na jednym ekranie
        wiersz = random.randint(0, 9)
        kolumna = random.randint(0, 9)
        pole = [kolumna * 64 + 20, wiersz * 64 + 20 + 640]  # wspó³rzêdne x i y œrodka przeszkody
        if not (pole in zajete_pola):                       # unikamy umieszczenie dwóch przeszkód w tym samym miejscu
            zajete_pola.append(pole)
            rodzaj = random.choice(["drzewko", "flaga"])
            if rodzaj == "drzewko": rysunek = "skier_tree.png"
            elif rodzaj == "flaga": rysunek = "skier_flag.png"
            przeszkoda = KlasaPrzeszkoda(rysunek, pole, rodzaj)
            przeszkody.add(przeszkoda)

# odmalowanie ekrany - ³¹cznie ze wszystkimi sprajtami
def animuj():
    ekran.fill([255, 255, 255])
    przeszkody.draw(ekran)
    ekran.blit(narciarz.image, narciarz.rect)    
    ekran.blit(wynik_tekst, [10, 10])
    pygame.display.flip()

# inicjalizacja
pygame.init()
ekran = pygame.display.set_mode([640,640])
zegar = pygame.time.Clock()
narciarz = KlasaNarciarz()
predkosc = [0, 6]
przeszkody = pygame.sprite.Group()  # grupa obiektór reprezentuj¹cych przeszkody
pozycja_mapy = 0
punkty = 0
utworz_mape()           # tworzymy ekran pe³en przeszkód
czcionka = pygame.font.Font(None, 50)

# g³ówna pêtla zdarzeñ Pygame
uruchomiona = True
while uruchomiona:
    zegar.tick(30)
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiona = False

        if zdarzenie.type == pygame.KEYDOWN:    # sprawdzamy, czy naciœniety zosta³ klawisz
            if zdarzenie.key == pygame.K_LEFT:  # lewa strza³ka powoduje skrêt w lewo
                predkosc = narciarz.obroc(-1)
            elif zdarzenie.key == pygame.K_RIGHT:   # prawa strza³ka powoduje skrêt w prawo
                predkosc = narciarz.obroc(1)
    narciarz.przesun(predkosc)                  # przesuniêcie narciarza (w lewo lub w prawo)
    pozycja_mapy += predkosc[1]                 # przesuniêcie przeszkód

    # Tworzymy nowy ekran pe³en przeszkód
    if pozycja_mapy >=640:
        utworz_mape()
        pozycja_mapy = 0

    # Sprawdzamy czy nast¹pi³o zderzenie z drzewkiem lub zebranie flagi
    kolizja = pygame.sprite.spritecollide(narciarz, przeszkody, False)
    if kolizja:
        if kolizja[0].rodzaj == "drzewko" and not kolizja[0].zaliczona: # kolizja z drzewkiem
            punkty = punkty - 100
            narciarz.image= pygame.image.load("skier_crash.png")    # obrazek narciarza po zderzeniu
            animuj()
            pygame.time.delay(1000)
            narciarz.image = pygame.image.load("skier_down.png")    # kontynuujemy szusowanie
            narciarz.nachylenie = 0
            predkosc = [0, 6]
            kolizja[0].zaliczona = True
        elif kolizja[0].rodzaj == "flaga" and not kolizja[0].zaliczona: # flaga zebrana
            punkty += 10
            kolizja[0].kill()                                       # usuniêcie flagi

    przeszkody.update()   
    wynik_tekst = czcionka.render("Wynik: " +str(punkty), 1, (0, 0, 0))
    animuj()
pygame.quit()

    
