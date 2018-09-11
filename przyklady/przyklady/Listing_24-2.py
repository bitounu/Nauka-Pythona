# Listing_24-2.py                                            
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Test szybkoœci pisania na klawiaturze 

import time, datetime, random, sys

zdania = [
    u"Na dnie kufra spoczywa³a sakiewka, a w niej kilka z³otych monet czarodziejskich.",
    u"Je¿eli on nie przestnie ciê ratowaæ, w koñcu ciê zabije.",
    u"To nasze decyzje, a nie zdolnoœci pokazuj¹, kim naprawdê jesteœmy.",
    u"Jestem czarodziejem, a nie jakimœ wymachuj¹cym kijem pawianem.",
    u"Wielkoœæ wzbudza zawiœæ, zawiœæ wywo³uje z³oœæ, z³oœæ rodzi k³amstwa.",
    u"W snach wkraczamy w œwiaty, które sami kreujemy.",
    u"W moim przekonaniu prawda ma wiêksz¹ wartoœæ ni¿ k³amstwa.",
    u"Œwit wydawa³ siê pod¹¿aæ za pó³noc¹ w nieprzyzwoitym poœpiechu."
    ]

# wyœwietlamy instrukcje
print u"Test szybkoœci pisania. Przepisz powy¿szy tekst. Zmierzê Ci czas."
time.sleep(2)
print "\nGotowy..."
time.sleep(1)
print "\nDo startu..."
time.sleep(1)
print "\nStart:"

zdanie = random.choice(zdania)  # wybieramy jedno zdanie z listy
print "\n " + zdanie
czas_poczatek = datetime.datetime.now() # w³¹czamy zegar
pisanie = raw_input('>').decode(sys.stdin.encoding)
czas_koniec = datetime.datetime.now()   # zatrzymujemy zegar
roznica = czas_koniec - czas_poczatek   # obliczamy czas, jaki up³yn¹³
pisanie_czas = roznica.seconds + roznica.microseconds / float(1000000)
zns = len(zdanie) / pisanie_czas
snm = zns * 60 / 5.0        # w przypadku testu szybkoœci pisania 1 s³owo = 5 znaków

# wyœwietlamy sformatowany wynik
print u"\nWprowadzi³eœ %i znaków w %.1f sekund." % (len(zdanie), pisanie_czas)
print u"Wynik to %.2f znaków na sekundê lub %.1f s³ów na minutê." %(zns, snm)
if pisanie == zdanie:
    print u"Nie pope³ni³eœ ¿adnego b³êdu."
else:
    print u"Ale pope³ni³eœ co najmniej jeden b³¹d."

