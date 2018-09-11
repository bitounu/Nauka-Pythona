# TIO_18-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 1, z rozdzia�u 18

# Ostateczna wersja gry PyPong, z poprawionym zachowaniem pi�ki
# podczas zderzenia z boczn� kraw�dzi� paletki


import sys, pygame

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
            self.predkosc[0] = -self.predkosc[0]

        # odbijamy pi�k� od g�rej i dolnej kraw�dzi okna
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
        Sprawdzamy, czy pi�ka znajduje si� "nad" paletk� lub "obok" paletki.
        Dzi�ki temu b�dziemy wiedzieli, w kt�rum kierunku odbi� pi�k�.

        Wyobra� sobie uko�n� lini� biegn�c� od lewego g�rnego r�gu paletki
        w g�r� i lew� stron�. Je�eli pi�ka znajdzie si� powy�ej tej linii
        uznamy, �e znajduje si� ona "nad" paletk�. Je�li pi�ka znajdzie si� poni�ej tej linii
        uznamy, �e znajduje si� "obok" paletki.
        Warto�� y-x wzd�u� tej linii jest sta�a. Powy�ej linii warto�� wyraz�nia y-x maleje,
        a poni�ej linii - ro�nie.
        Tak wi�c, je�li warto�� y-x w przypadku pi�ki b�dzie mniejsza ni� warto�� y-x paletki,
        oznacza to, �e pi�ka znajduje si� "nad" paletk� (powinna si� odbi� do g�ry).
        Je�li warto�� y-x w przypadku pi�ki b�dzie wi�ksza ni� warto�� y-x paletki,
        oznacza to, �e pi�ka znajduje sie "obok" paletki, wi�c powinna si� odbi� na bok.
        Por�wnujemy ze sob� g�rny lewy r�g paletki i dolny prawy r�g pi�ki.

        Po drugiej stronie paletki, uko�na linia biegnie od g�rnego prawego rogu paletki
        w g�r� i praw� stron�. W tym przypadku, to warto�� y+x b�dzie sta�a wzd�u� tej linii,
        a je�eli warto�� y+x w przypadku pi�ki b�dzie mniejsza ni� warto�� y+x w przypadku paletki,
        pi�ka znajduje si� "nad" paletk� i odbijemy j� w g�r�. Je�eli warto�� y+x w przypadku pi�ki b�dzie wi�ksza,
        pi�ka znajduje si� "obok" paletki i odbijemy j� na bok.
             
        Poni�sze wzory implementuj� to rozwi�zanie.
        """     
        pal_gl_y_min_x = paletka.rect.topleft[1] - paletka.rect.topleft[0]
        pal_gp_y_plus_x = paletka.rect.topright[1] + paletka.rect.topright[0]
        pil_dp_y_min_x = mojaPilka.rect.bottomright[1] - mojaPilka.rect.bottomright[0]
        pil_dl_y_plus_x = mojaPilka.rect.bottomleft[1] + mojaPilka.rect.bottomleft[0]
                
        if (pil_dp_y_min_x > pal_gl_y_min_x  or pil_dl_y_plus_x > pal_gp_y_plus_x):
            # "obok" paletki, wi�c odbijamy w osi x
            mojaPilka.predkosc[0] = -mojaPilka.predkosc[0]
        else:
            # "nad" paletk�, wi�c odbijamy w osi y
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
