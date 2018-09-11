# Listing_19-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# PyPong z dŸwiêkami i muzyk¹

import sys, pygame

class KlasaMojaPilka(pygame.sprite.Sprite):
    def __init__(self, plik_obrazka, predkosc, polozenie):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(plik_obrazka)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
        self.predkosc = predkosc

    def przesun(self):
        global wynik, wynik_czcionka, wynik_powierzchnia
        self.rect = self.rect.move(self.predkosc)
        if self.rect.left < 0 or self.rect.right > ekran.get_width():
            self.predkosc[0] = -self.predkosc[0]
            if self.rect.top < ekran.get_height():
                uderzenie_sciana.play()             # Odtwarzamy dŸwiêk gdy pi³ka uderzy o boczn¹ krawêdŸ

        if self.rect.top <= 0 :            
            self.predkosc[1] = -self.predkosc[1]
            wynik = wynik + 1
            wynik_powierzchnia = wynik_czcionka.render(str(wynik), 1, (0, 0, 0))
            zdobyty_punkt.play()                # Odtwarzamy dŸwiêk gdy pi³ka uderzy w górn¹ krawêdŸ 
                                                #   (gracz zdobêdzie punkt)

class KlasaMojaPaletka(pygame.sprite.Sprite):
    def __init__(self, polozenie):
        pygame.sprite.Sprite.__init__(self)
        obrazek_powierzchnia = pygame.surface.Surface([100, 20])
        obrazek_powierzchnia.fill([0,0,0])
        self.image = obrazek_powierzchnia.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = polozenie
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("bg_music.mp3")                     # £adujemy plik z muzyk¹
pygame.mixer.music.set_volume(0.30)                         # Ustawiamy poziom g³oœnoœci muzyki
pygame.mixer.music.play(-1)                                 # Zaczynamy odtwarzanie muzyki (z powtarzaniem)
uderzenie = pygame.mixer.Sound("hit_paddle.wav")            # £adujemy pozosta³e dŸwiêki
uderzenie.set_volume(0.4)                                   # i ustawiamy ich poziom g³oœnoœci 
nowe_zycie = pygame.mixer.Sound("new_life.wav")             #
nowe_zycie.set_volume(0.5)                                  #
plask = pygame.mixer.Sound("splat.wav")                     #
plask.set_volume(0.6)                                       #
uderzenie_sciana = pygame.mixer.Sound("hit_wall.wav")       #
uderzenie_sciana.set_volume(0.4)                            #
zdobyty_punkt = pygame.mixer.Sound("get_point.wav")         #
zdobyty_punkt.set_volume(0.2)                               #
papa = pygame.mixer.Sound("game_over.wav")                  #
papa.set_volume(0.6)                                        #

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
        uderzenie.play()                # Odtwarzamy dŸwiêk gdy pi³ka uderzy w paletkê
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
        if not koniec:
            plask.play()            # Odtwarzamy dŸwiêk gdy gracz straci ¿ycie
        zycia = zycia - 1
        if zycia == 0:
            if not koniec:
                pygame.time.delay(1000)      # Czekamy sekundê  
                papa.play()                  # i odtwarzamy dŸwiêk koñcowy
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
            pygame.mixer.music.fadeout(2000)        # Wyciszamy muzykê
        else:
            pygame.time.delay(1000)
            nowe_zycie.play()           # Odtwarzamy dŸwiêk gdy gracz rozpoczyna grê z nowym ¿yciem
            mojaPilka.rect.topleft = [50, 50]
            ekran.blit(mojaPilka.image, mojaPilka.rect)
            pygame.display.flip()
            pygame.time.delay(1000)
pygame.quit()

