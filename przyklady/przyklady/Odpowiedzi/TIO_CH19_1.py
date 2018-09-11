# TIO_CH19_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 1, z rozdzia³u 19.

# Gra w odgadywanie liczby z dodanymi dŸwiêkami

import random, pygame, sys
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode([200,100])  # tworzymy ma³e okno Pygame

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

sekret = random.randint(1, 100)     # wybieramy tajemne s³owo
propozycja = 0
proba = 0

print "AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadkê!"
print "Jest ni¹ tajemna liczba od 1 do 99. Na odgadniêcie jej masz 6 prób."
ahoj.play()
pygame.time.delay(8000)  # czekamy, a¿ dŸwiêk siê zakoñczy odtwarzaæ

# Gracz ma do wykorzystania tylko 6 prób
uruchomiony = True
while uruchomiony:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            uruchomiony = False

    while propozycja != sekret and proba < 6:
        jakaLiczba.play()
        propozycja = input("Jaka to liczba?") # Pobranie propozycji gracza
        if propozycja < sekret:
            print "Za ma³a, psubracie!"
            zaMala.play()
            pygame.time.delay(2200)   # czekamy, a¿ dŸwiêk siê zakoñczy odtwarzaæ
        elif propozycja > sekret:
            print "Za du¿a, szczurze l¹dowy!"
            zaDuza.play()
            pygame.time.delay(1800)   # czekamy, a¿ dŸwiêk siê zakoñczy odtwarzaæ
        proba = proba + 1 # Zwiêkszenie liczby prób

    # Wyœwietlenie komunikatu na koñcu rozgrywki
    if propozycja == sekret:
        print "Stop! Uda³o Ci siê! Odgad³eœ moj¹ tajemn¹ liczbê!"
        odgadles.play()
        pygame.time.delay(3200)   # czekamy, a¿ dŸwiêk siê zakoñczy odtwarzaæ
        uruchomiony = False
    else:
        print "Wykorzysta³eœ wszystkie próby! Powodzenia nastêpnym razem, kole¿ko!"
        print "Tajemna liczba to", sekret
        koniec.play()
        pygame.time.delay(3700)   # czekamy, a¿ dŸwiêk siê zakoñczy odtwarzaæ
        uruchomiony = False
pygame.quit()
