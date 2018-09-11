# -*- coding: utf-8 -*-
# Listing_23-8.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone ósemki - sprawdzamy jaką decyzję podjął gracz

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

print u"Co chcesz zrobić? ",
odpowiedz = raw_input (u"Wprowadź nazwę karty lub wpisz 'Dobierz', aby dobrać kartę: " )

dobre_zagranie = False

# Wykonujemy pętlę, aż gracz wskaże poprawną kartę
while not dobre_zagranie:
    wybrana_karta = None        # Gracz wybiera kartę którą ma na ręce lub dobiera nową
    while wybrana_karta == None:
        if odpowiedz.lower() == 'dobierz':
            # Jeżeli dobiera — usuwamy kartę ze stosu
            # i dodajemy na rękę gracza
            dobre_zagranie = True
            if len(talia) > 0:
                karta = random.choice(talia)
                reka_gracza.append(karta)
                talia.remove(karta)
                print u"Dobrałeś", karta.krotka_nazwa
            else:
                print u"Na stosie nie ma już kart"
                zablokowani += 1
            return
        else:
            for karta in reka_gracza:       # Sprawdzamy, czy wybrana karta znajduje się na ręce gracza 
                if odpowiedz.upper() == karta.krotka_nazwa:
                    wybrana_karta = karta
            if wybrana_karta == None:
                odpowiedz = raw_input(u"Nie masz na ręce tej karty. Spróbuj ponownie:")

    if wybrana_karta.figura == '8':         # Zagranie 8 jest zawsze prawidłowym zagraniem
        dobre_zagranie = True
        czy_osemka = True
    elif wybrana_karta.kolor == kolor_wiodacy:
        dobre_zagranie = True
    elif wybrana_karta.figura == karta_wiodaca.figura:
        dobre_zagranie = True

    if not dobre_zagranie:
        odpowiedz = raw_input(u"Nieprawidłowe zagranie. Spróbuj ponownie: ")
