# TIO_CH19_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 1, z rozdzia�u 19.

# Gra w odgadywanie liczby z dodanymi d�wi�kami

import random, pygame, sys
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode([200,100])  # tworzymy ma�e okno Pygame

ahoj = pygame.mixer.Sound("Ahoy.wav")
zaMala = pygame.mixer.Sound("TooLow.wav")
zaDuza = pygame.mixer.Sound("TooHigh.wav")
jakaLiczba = pygame.mixer.Sound("WhatsYerGuess.wav")
odgadles = pygame.mixer.Sound("AvastGotIt.wav")
koniec = pygame.mixer.Sound("NoMore.wav")

ahoj.set_volume(0.4)
zaMala.set_volume(0.4)
zaDuza.set_volume(0.4)
jakaLiczba.set_volume(0.4)
odgadles.set_volume(0.4)
koniec.set_volume(0.4)

sekret = random.randint(1, 100)     # wybieramy tajemne s�owo
propozycja = 0
proba = 0

print "AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadk�!"
print "Jest ni� tajemna liczba od 1 do 99. Na odgadni�cie jej masz 6 pr�b."
ahoj.play()
pygame.time.delay(8000)  # czekamy, a� d�wi�k si� zako�czy odtwarza�

# Gracz ma do wykorzystania tylko 6 pr�b
uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False

    while propozycja != sekret and proba < 6:
        jakaLiczba.play()
        propozycja = input("Jaka to liczba?") # Pobranie propozycji gracza
        if propozycja < sekret:
            print "Za ma�a, psubracie!"
            zaMala.play()
            pygame.time.delay(2200)   # czekamy, a� d�wi�k si� zako�czy odtwarza�
        elif propozycja > sekret:
            print "Za du�a, szczurze l�dowy!"
            zaDuza.play()
            pygame.time.delay(1800)   # czekamy, a� d�wi�k si� zako�czy odtwarza�
        proba = proba + 1 # Zwi�kszenie liczby pr�b

    # Wy�wietlenie komunikatu na ko�cu rozgrywki
    if propozycja == sekret:
        print "Stop! Uda�o Ci si�! Odgad�e� moj� tajemn� liczb�!"
        odgadles.play()
        pygame.time.delay(3200)   # czekamy, a� d�wi�k si� zako�czy odtwarza�
        uruchomiony = False
    else:
        print "Wykorzysta�e� wszystkie pr�by! Powodzenia nast�pnym razem, kole�ko!"
        print "Tajemna liczba to", sekret
        koniec.play()
        pygame.time.delay(3700)   # czekamy, a� d�wi�k si� zako�czy odtwarza�
        uruchomiony = False
pygame.quit()
