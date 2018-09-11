# -*- coding: utf-8 -*-
# Listing_23-11.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone Ăłsemki - obliczanie liczby punktĂłw w gĹ‚Ăłwnej pÄ™tli programu

# ZwrĂłÄ‡ uwagÄ™, ĹĽe to nie jest kompletny program.  Aby utowrzyÄ‡ kompletny program gry w Szalone Ăłsemki,
#   naleĹĽy poĹ‚Ä…czyÄ‡ poniĹĽszy kod z posostaĹ‚ymi elemenatmi.

koniec = False
gracz_razem = komp_razem = 0
while not koniec:
    koniec_partii = False

    zablokowani = 0
    inicjalizacja_kart()        # Tworzymy taliÄ™ i rozdajemy karty na rÄ™kÄ™ gracza i komputera
    while not koniec_partii:
        tura_gracza()
        if len(reka_gracza) == 0:   # Wygrywa gracz
            koniec_partii = True
            print
            print u"WygraĹ‚eĹ›!"
            # wyĹ›wietlamy wynik
            gracz_punkty = 0
            for karta in reka_komputera:
                gracz_punkty += karta.wartosc       # Dodajemy punkty z kart, jakie zostaĹ‚y na rÄ™ce komputera
            gracz_razem += gracz_punkty             # Dodajemy punkty zdobyte w tej partii, do sumarycznej liczby punktĂłw
            print u"OtrzymaĹ‚eĹ› %i punktĂłw z kart na rÄ™ce komptera" % gracz_punkty

        if not koniec_partii:
            tura_komputera()
        if len(reka_komputera) == 0:        # Wygrywa komputer
            koniec_partii = True
            print
            print u"WygraĹ‚ komputer!"
            # wyĹ›wietlamy wynik
            komp_punkty = 0
            for karta in reka_gracza:
                komp_punkty += karta.wartosc        # Dodajemy punkty z kart, jakie zostaĹ‚y na rÄ™ce gracza
            komp_razem += komp_punkty               # Dodajemy zdobyte punkty w tej partii, do sumarycznej liczby punktĂłw
            print u"Komputer otrzymaĹ‚ %i punktĂłw z kart na Twojej rÄ™ce" % komp_punkty
        if zablokowani >= 2:                        # Obaj grasz sÄ… zablokowani, wiÄ™c oboje zdobywajÄ… punkty
            koniec_partii = True
            print u"Obaj zawodnicy sÄ… zablokowani. KONIEC GRY."
            gracz_punkty = 0
            for karta in reka_komputera:
                gracz_punkty += karta.wartosc
            gracz_razem += gracz_punkty
            komp_punkty = 0
            for karta in reka_gracza:
                komp_punkty += karta.wartosc
            komp_razem += komp_punkty
            # WyĹ›wietlamy punkty zdobyte w partii
            print u"OtrzymaĹ‚eĹ› %i punktĂłw z kart na rÄ™ce komptera" % gracz_punkty
            print u"Komputer otrzymaĹ‚ %i punktĂłw z kart na Twojej rÄ™ce" % komp_punkty
    jeszcze_raz = raw_input("Jeszcze jedna partia (T/N)? ")
    if jeszcze_raz.lower().startswith('t'):
        koniec = False
        # WyĹ›wietlamy caĹ‚kowitÄ… liczbÄ™ punktĂłw
        print u"\nZdobyĹ‚eĹ› do tej pory %i punktĂłw" % gracz_razem
        print u"a komputer zdobyĹ‚ %i punktĂłw.\n" % komp_razem
    else:
        koniec = True

# WyĹ›wietlamy koĹ„cowy wynik
print u"\n KoĹ„cowy wynik:"
print "Ty: %i Komputer: %i" % (gracz_razem, komp_razem)

