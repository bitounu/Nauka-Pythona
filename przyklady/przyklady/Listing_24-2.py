# Listing_24-2.py                                            
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Test szybko�ci pisania na klawiaturze 

import time, datetime, random, sys

zdania = [
    u"Na dnie kufra spoczywa�a sakiewka, a w niej kilka z�otych monet czarodziejskich.",
    u"Je�eli on nie przestnie ci� ratowa�, w ko�cu ci� zabije.",
    u"To nasze decyzje, a nie zdolno�ci pokazuj�, kim naprawd� jeste�my.",
    u"Jestem czarodziejem, a nie jakim� wymachuj�cym kijem pawianem.",
    u"Wielko�� wzbudza zawi��, zawi�� wywo�uje z�o��, z�o�� rodzi k�amstwa.",
    u"W snach wkraczamy w �wiaty, kt�re sami kreujemy.",
    u"W moim przekonaniu prawda ma wi�ksz� warto�� ni� k�amstwa.",
    u"�wit wydawa� si� pod��a� za p�noc� w nieprzyzwoitym po�piechu."
    ]

# wy�wietlamy instrukcje
print u"Test szybko�ci pisania. Przepisz powy�szy tekst. Zmierz� Ci czas."
time.sleep(2)
print "\nGotowy..."
time.sleep(1)
print "\nDo startu..."
time.sleep(1)
print "\nStart:"

zdanie = random.choice(zdania)  # wybieramy jedno zdanie z listy
print "\n " + zdanie
czas_poczatek = datetime.datetime.now() # w��czamy zegar
pisanie = raw_input('>').decode(sys.stdin.encoding)
czas_koniec = datetime.datetime.now()   # zatrzymujemy zegar
roznica = czas_koniec - czas_poczatek   # obliczamy czas, jaki up�yn��
pisanie_czas = roznica.seconds + roznica.microseconds / float(1000000)
zns = len(zdanie) / pisanie_czas
snm = zns * 60 / 5.0        # w przypadku testu szybko�ci pisania 1 s�owo = 5 znak�w

# wy�wietlamy sformatowany wynik
print u"\nWprowadzi�e� %i znak�w w %.1f sekund." % (len(zdanie), pisanie_czas)
print u"Wynik to %.2f znak�w na sekund� lub %.1f s��w na minut�." %(zns, snm)
if pisanie == zdanie:
    print u"Nie pope�ni�e� �adnego b��du."
else:
    print u"Ale pope�ni�e� co najmniej jeden b��d."

