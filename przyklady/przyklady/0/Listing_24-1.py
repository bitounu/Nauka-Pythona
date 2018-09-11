# -*- coding: utf-8 -*-
# Listing_24-1.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# LÄ…downik KsiÄ™ĹĽycowy
# symulacja komputerowa lÄ…dowania statku kosmicznego

# Inicjalizacja programu
import pygame, sys

pygame.init()
ekran = pygame.display.set_mode([400,600])
ekran.fill([0, 0, 0])
statek = pygame.image.load('lunarlander.png')
ksiezyc = pygame.image.load('moonsurface.png')
ziemia = 540 # Platforma do lÄ…dowania znajduje siÄ™ na y = 540
poczatek = 90
zegar = pygame.time.Clock()
statek_masa= 5000.0
paliwo = 5000.0
predkosc = -100.0
grawitacja = 10
wysokosc = 2000
sila_ciagu = 0
delta_v = 0
polozenie_y = 90
przytrzymany = False

# Tworzymy siĹ‚Ä™ ciÄ…gu
class KlasaSilaCiagu(pygame.sprite.Sprite):
    def __init__(self, polozenie = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        powierzchnia_rysunku = pygame.surface.Surface([30, 10])
        powierzchnia_rysunku.fill([128,128,128])
        self.image = powierzchnia_rysunku.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = polozenie

# Obliczamy wysokoĹ›Ä‡, prÄ™dkoĹ›Ä‡, przyspieszenie i iloĹ›Ä‡ paliwa
def oblicz_predkosc():
    global sila_ciagu, paliwo, predkosc, delta_v, wysokosc, polozenie_y
    delta_t = 1/fps
    sila_ciagu = (500 - mojaSilaCiagu.rect.centery) * 5.0  # Zamieniamy wspĂłĹ‚rzÄ™dnÄ… y regulatora siĹ‚y ciÄ…gu
                                                           # na siĹ‚Ä™ ciÄ…gu
    paliwo -= sila_ciagu /(10 * fps)                      # Zmniejszamy iloĹ›Ä‡ paliwa
    if paliwo < 0: paliwo = 0.0
    if paliwo < 0.1: sila_ciagu = 0.0
    delta_v = delta_t * (-grawitacja + 200 * sila_ciagu / (statek_masa+ paliwo))
    predkosc = predkosc + delta_v
    delta_h = predkosc * delta_t
    wysokosc = wysokosc + delta_h
    polozenie_y = ziemia - (wysokosc * (ziemia - poczatek) / 2000) - 90

# WyĹ›wietlamy tekst informujÄ…cy o prÄ™dkoĹ›ci, wysokoĹ›ci itp. 
def wyswietl_statystyki():
    pred_lancuch = u"prÄ™dkoĹ›Ä‡: %i m/s" % predkosc
    wys_lancuch = u"wysokoĹ›Ä‡: %.1f" % wysokosc
    sila_lancuch = u"siĹ‚a ciÄ…gu: %i" % sila_ciagu
    przysp_lancuch = "przyspieszenie: %.1f" % (delta_v * fps)
    pal_lancuch = "paliwo: %i" % paliwo
    pred_czcionka = pygame.font.Font(None, 26)
    pred_pow = pred_czcionka.render(pred_lancuch, 1, (255, 255, 255))
    ekran.blit(pred_pow, [10, 50])
    przysp_czcionka = pygame.font.Font(None, 26)
    przysp_pow = przysp_czcionka.render(przysp_lancuch, 1, (255, 255, 255))
    ekran.blit(przysp_pow, [10, 100])
    wys_czcionka = pygame.font.Font(None, 26)
    wys_pow = wys_czcionka.render(wys_lancuch, 1, (255, 255, 255))
    ekran.blit(wys_pow, [10, 150])
    sila_czcionka = pygame.font.Font(None, 26)
    sila_pow = sila_czcionka.render(sila_lancuch, 1, (255, 255, 255))
    ekran.blit(sila_pow, [10, 200])
    pal_czcionka = pygame.font.Font(None, 26)
    pal_pow = pal_czcionka.render(pal_lancuch, 1, (255, 255, 255))
    ekran.blit(pal_pow, [60, 300])

# Rysujemy pĹ‚omieĹ„ o wielkoĹ›ci zaleĹĽnej od siĹ‚y ciÄ…gu
def wyswietl_plomienie():
    rozmiar_plomienia = sila_ciagu / 15
    for i in range (2):
        poczatekx = 252 - 10 + i * 19
        poczateky = polozenie_y + 83
        pygame.draw.polygon(ekran, [255, 109, 14], [(poczatekx, poczateky),
                                    (poczatekx + 4, poczateky + rozmiar_plomienia),
                                    (poczatekx + 8, poczateky)], 0)
        
# Kiedy gra siÄ™ skoĹ„czy, wyĹ›wietlamy statystyki koĹ„cowe
def wyswietl_podsumowanie():
    podsum1 = "Koniec gry"
    podsum2 = u"WylÄ…dowaĹ‚eĹ› z pr. %.1f m/s" % predkosc
    if predkosc > -5:
        podsum3 = u"PiÄ™kne lÄ…dowanie!"
        podsum4 = u"SĹ‚yszaĹ‚em, ĹĽe NASA prowadzi nabĂłr!"
    elif predkosc > -15:
        podsum3 = u"Ufff! Twarde lÄ…dowanie, ale siÄ™ udaĹ‚o."
        podsum4 = u"NastÄ™pnym razem pĂłjdzie Ci lepiej."
    else:
        podsum3 = u"Ups! ZniszczyĹ‚eĹ› statek wart 30 mld dolarĂłw!"
        podsum4 = u"Jak teraz wrĂłcimy na ZiemiÄ™?"
    pygame.draw.rect(ekran, [0, 0, 0], [5, 5, 350, 280],0)
    p1_czcionka = pygame.font.Font(None, 70)
    p1_pow = p1_czcionka.render(podsum1, 1, (255, 255, 255))
    ekran.blit(p1_pow, [20, 50])
    p2_czcionka = pygame.font.Font(None, 40)
    p2_pow = p2_czcionka.render(podsum2, 1, (255, 255, 255))
    ekran.blit(p2_pow, [20, 110])
    p3_czcionka = pygame.font.Font(None, 26)
    p3_pow = p3_czcionka.render(podsum3, 1, (255, 255, 255))
    ekran.blit(p3_pow, [20, 150])
    p4_czcionka = pygame.font.Font(None, 26)
    p4_pow = p4_czcionka.render(podsum4, 1, (255, 255, 255))
    ekran.blit(p4_pow, [20, 180])
    pygame.display.flip()

mojaSilaCiagu = KlasaSilaCiagu([15, 500])

# GĹ‚Ăłwna pÄ™tla
uruchomiona = True
while uruchomiona:
    zegar.tick(30)
    fps = zegar.get_fps()
    if fps < 1: fps = 30
    if wysokosc > 0.01:
        oblicz_predkosc()
        ekran.fill([0, 0, 0])
        wyswietl_statystyki()
        pygame.draw.rect(ekran, [0, 0, 255], [80, 350, 24, 100], 2)
        wskaznikPaliwa = 96 * paliwo / 5000
        pygame.draw.rect(ekran, [0,255,0],
               [84,448-wskaznikPaliwa,18, wskaznikPaliwa], 0)
        pygame.draw.rect(ekran, [255, 0, 0],[25, 300, 10, 200],0)  # Zarys regulatora siĹ‚y ciÄ…gu 
        ekran.blit(ksiezyc, [0, 500, 400, 100])     # KsiÄ™ĹĽyc
        pygame.draw.rect(ekran, [60, 60, 60],[220, 535, 70, 5],0) # Platforma do lÄ…dowania
        ekran.blit(mojaSilaCiagu.image, mojaSilaCiagu.rect)  # Suwak regulatora siĹ‚y ciÄ…gu
        wyswietl_plomienie()        # PĹ‚omienie
        ekran.blit(statek, [230, polozenie_y, 50, 90])  # Statek
        instrukcja1 = u"WylÄ…duj, zanim skoĹ„czy siÄ™ paliwo."
        instrukcja2 = u"Dobre lÄ…dowanie: < 15m/s DoskonaĹ‚e lÄ…dowanie: < 5m/s"
        inst1_czcionka = pygame.font.Font(None, 20)
        inst1_powierzchnia = inst1_czcionka.render(instrukcja1, 1, (255, 255, 255))
        ekran.blit(inst1_powierzchnia, [10, 550])
        inst2_czcionka = pygame.font.Font(None, 20)
        inst2_powierzchnia = inst1_czcionka.render(instrukcja2, 1, (255, 255, 255))
        ekran.blit(inst2_powierzchnia, [10, 575])
        pygame.display.flip()
        
    else:           # Koniec gry. WyĹ›wietlamy wynik koĹ„cowy
        wyswietl_podsumowanie()

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiona = False
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            przytrzymany = True
        elif zdarzenie.type == pygame.MOUSEBUTTONUP:
            przytrzymany = False
        elif zdarzenie.type == pygame.MOUSEMOTION:
            if przytrzymany:
                mojaSilaCiagu.rect.centery = zdarzenie.pos[1]
                if mojaSilaCiagu.rect.centery < 300:
                    mojaSilaCiagu.rect.centery = 300
                if mojaSilaCiagu.rect.centery > 500:
                    mojaSilaCiagu.rect.centery = 500
pygame.quit()


