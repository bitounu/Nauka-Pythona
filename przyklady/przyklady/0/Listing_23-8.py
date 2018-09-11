# -*- coding: utf-8 -*-
# Listing_23-8.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone Ăłsemki - sprawdzamy jakÄ… decyzjÄ™ podjÄ…Ĺ‚ gracz

# ZwrĂłÄ‡ uwagÄ™, ĹĽe to nie jest kompletny program.  Aby utowrzyÄ‡ kompletny program gry w Szalone Ăłsemki,
#   naleĹĽy poĹ‚Ä…czyÄ‡ poniĹĽszy kod z posostaĹ‚ymi elemenatmi.

print u"Co chcesz zrobiÄ‡? ",
odpowiedz = raw_input (u"WprowadĹş nazwÄ™ karty lub wpisz 'Dobierz', aby dobraÄ‡ kartÄ™: " )

dobre_zagranie = False

# Wykonujemy pÄ™tlÄ™, aĹĽ gracz wskaĹĽe poprawnÄ… kartÄ™
while not dobre_zagranie:
    wybrana_karta = None        # Gracz wybiera kartÄ™ ktĂłrÄ… ma na rÄ™ce lub dobiera nowÄ…
    while wybrana_karta == None:
        if odpowiedz.lower() == 'dobierz':
            # JeĹĽeli dobiera â€” usuwamy kartÄ™ ze stosu
            # i dodajemy na rÄ™kÄ™ gracza
            dobre_zagranie = True
            if len(talia) > 0:
                karta = random.choice(talia)
                reka_gracza.append(karta)
                talia.remove(karta)
                print u"DobraĹ‚eĹ›", karta.krotka_nazwa
            else:
                print u"Na stosie nie ma juĹĽ kart"
                zablokowani += 1
            return
        else:
            for karta in reka_gracza:       # Sprawdzamy, czy wybrana karta znajduje siÄ™ na rÄ™ce gracza 
                if odpowiedz.upper() == karta.krotka_nazwa:
                    wybrana_karta = karta
            if wybrana_karta == None:
                odpowiedz = raw_input(u"Nie masz na rÄ™ce tej karty. SprĂłbuj ponownie:")

    if wybrana_karta.figura == '8':         # Zagranie 8 jest zawsze prawidĹ‚owym zagraniem
        dobre_zagranie = True
        czy_osemka = True
    elif wybrana_karta.kolor == kolor_wiodacy:
        dobre_zagranie = True
    elif wybrana_karta.figura == karta_wiodaca.figura:
        dobre_zagranie = True

    if not dobre_zagranie:
        odpowiedz = raw_input(u"NieprawidĹ‚owe zagranie. SprĂłbuj ponownie: ")
