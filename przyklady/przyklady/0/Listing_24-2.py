# Listing_24-2.py                                            
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Test szybkości pisania na klawiaturze 

import time, datetime, random, sys

zdania = [
    u"Na dnie kufra spoczywała sakiewka, a w niej kilka złotych monet czarodziejskich.",
    u"Jeżeli on nie przestnie cię ratować, w końcu cię zabije.",
    u"To nasze decyzje, a nie zdolności pokazują, kim naprawdę jesteśmy.",
    u"Jestem czarodziejem, a nie jakimś wymachującym kijem pawianem.",
    u"Wielkość wzbudza zawiść, zawiść wywołuje złość, złość rodzi kłamstwa.",
    u"W snach wkraczamy w światy, które sami kreujemy.",
    u"W moim przekonaniu prawda ma większą wartość niż kłamstwa.",
    u"Świt wydawał się podążać za północą w nieprzyzwoitym pośpiechu."
    ]

# wyświetlamy instrukcje
print u"Test szybkości pisania. Przepisz powyższy tekst. Zmierzę Ci czas."
time.sleep(2)
print "\nGotowy..."
time.sleep(1)
print "\nDo startu..."
time.sleep(1)
print "\nStart:"

zdanie = random.choice(zdania)  # wybieramy jedno zdanie z listy
print "\n " + zdanie
czas_poczatek = datetime.datetime.now() # włączamy zegar
pisanie = raw_input('>').decode(sys.stdin.encoding)
czas_koniec = datetime.datetime.now()   # zatrzymujemy zegar
roznica = czas_koniec - czas_poczatek   # obliczamy czas, jaki upłynął
pisanie_czas = roznica.seconds + roznica.microseconds / float(1000000)
zns = len(zdanie) / pisanie_czas
snm = zns * 60 / 5.0        # w przypadku testu szybkości pisania 1 słowo = 5 znaków

# wyświetlamy sformatowany wynik
print u"\nWprowadziłeś %i znaków w %.1f sekund." % (len(zdanie), pisanie_czas)
print u"Wynik to %.2f znaków na sekundę lub %.1f słów na minutę." %(zns, snm)
if pisanie == zdanie:
    print u"Nie popełniłeś żadnego błędu."
else:
    print u"Ale popełniłeś co najmniej jeden błąd."

