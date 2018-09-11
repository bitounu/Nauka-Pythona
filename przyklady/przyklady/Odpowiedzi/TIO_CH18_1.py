# TIO_18-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 1, z rozdzia³u 18

# Ostateczna wersja gry PyPong, z poprawionym zachowaniem pi³ki
# podczas zderzenia z boczn¹ krawêdzi¹ paletki


import sys, pygame

class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, predkosc, polozenie):
        pygame.sprite.Sprite.__init__(self)      # wywo³ujemy inicjalizator klasu Sprite 
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc

    def przesun(self):
        global wynik, wynik_czcionka, wynik_powierzchnia
        self.rect = self.rect.move(self.predkosc)
        # odbijamy pi³kê od bocznych krawêdzi okna
        if self.rect.left < 0 or self.rect.right > ekran.get_width():
            self.predkosc[0] = -self.predkosc[0]

        # odbijamy pi³kê od górej i dolnej krawêdzi okna
        if self.rect.top <= 0 :            
            self.predkosc[1] = -self.predkosc[1]
            wynik = wynik + 1
            wynik_powierzchnia = wynik_czcionka.render(str(wynik), 1, (0, 0, 0))

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
         
        """
        Sprawdzamy, czy pi³ka znajduje siê "nad" paletk¹ lub "obok" paletki.
        Dziêki temu bêdziemy wiedzieli, w którum kierunku odbiæ pi³kê.

        WyobraŸ sobie ukoœn¹ liniê biegn¹c¹ od lewego górnego rógu paletki
        w górê i lew¹ stronê. Je¿eli pi³ka znajdzie siê powy¿ej tej linii
        uznamy, ¿e znajduje siê ona "nad" paletk¹. Je¿li pi³ka znajdzie siê poni¿ej tej linii
        uznamy, ¿e znajduje siê "obok" paletki.
        Wartoœæ y-x wzd³u¿ tej linii jest sta³a. Powy¿ej linii wartoœæ wyrazênia y-x maleje,
        a poni¿ej linii - roœnie.
        Tak wiêc, jeœli wartoœæ y-x w przypadku pi³ki bêdzie mniejsza ni¿ wartoœæ y-x paletki,
        oznacza to, ¿e pi³ka znajduje siê "nad" paletk¹ (powinna siê odbiæ do góry).
        Jeœli wartoœæ y-x w przypadku pi³ki bêdzie wiêksza ni¿ wartoœæ y-x paletki,
        oznacza to, ¿e pi³ka znajduje sie "obok" paletki, wiêc powinna siê odbiæ na bok.
        Porównujemy ze sob¹ górny lewy róg paletki i dolny prawy róg pi³ki.

        Po drugiej stronie paletki, ukoœna linia biegnie od górnego prawego rogu paletki
        w górê i praw¹ stronê. W tym przypadku, to wartoœæ y+x bêdzie sta³a wzd³u¿ tej linii,
        a je¿eli wartoœæ y+x w przypadku pi³ki bêdzie mniejsza ni¿ wartoœæ y+x w przypadku paletki,
        pi³ka znajduje siê "nad" paletk¹ i odbijemy j¹ w górê. Je¿eli wartoœæ y+x w przypadku pi³ki bêdzie wiêksza,
        pi³ka znajduje siê "obok" paletki i odbijemy j¹ na bok.
             
        Poni¿sze wzory implementuj¹ to rozwi¹zanie.
        """     
        pal_gl_y_min_x = paletka.rect.topleft[1] - paletka.rect.topleft[0]
        pal_gp_y_plus_x = paletka.rect.topright[1] + paletka.rect.topright[0]
        pil_dp_y_min_x = mojaPilka.rect.bottomright[1] - mojaPilka.rect.bottomright[0]
        pil_dl_y_plus_x = mojaPilka.rect.bottomleft[1] + mojaPilka.rect.bottomleft[0]
                
        if (pil_dp_y_min_x > pal_gl_y_min_x  or pil_dl_y_plus_x > pal_gp_y_plus_x):
            # "obok" paletki, wiêc odbijamy w osi x
            mojaPilka.predkosc[0] = -mojaPilka.predkosc[0]
        else:
            # "nad" paletk¹, wiêc odbijamy w osi y
            mojaPilka.predkosc[1] = -mojaPilka.predkosc[1]
            
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
        # tracimy jedno ¿ycie, gdy pi³ka wypadnie poza doln¹ krawêdŸ okna
        zycia = zycia - 1
        if zycia == 0:
            koncowy_tekst1 = "Koniec gry"
            koncowy_tekst2 = "Twój wynik to: " + str(wynik)
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
            pygame.time.delay(2000) # czekamy 2 sekundy i ponownie wprowadzamy do gry pi³kê
            mojaPilka.rect.topleft = [(ekran.get_rect().width) - 40*zycia, 20]    
pygame.quit()
