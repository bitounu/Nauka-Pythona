# -*- coding: utf-8 -*-
# Listing_23-11.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone ósemki - obliczanie liczby punktów w głównej pętli programu

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

koniec = False
gracz_razem = komp_razem = 0
while not koniec:
    koniec_partii = False

    zablokowani = 0
    inicjalizacja_kart()        # Tworzymy talię i rozdajemy karty na rękę gracza i komputera
    while not koniec_partii:
        tura_gracza()
        if len(reka_gracza) == 0:   # Wygrywa gracz
            koniec_partii = True
            print
            print u"Wygrałeś!"
            # wyświetlamy wynik
            gracz_punkty = 0
            for karta in reka_komputera:
                gracz_punkty += karta.wartosc       # Dodajemy punkty z kart, jakie zostały na ręce komputera
            gracz_razem += gracz_punkty             # Dodajemy punkty zdobyte w tej partii, do sumarycznej liczby punktów
            print u"Otrzymałeś %i punktów z kart na ręce komptera" % gracz_punkty

        if not koniec_partii:
            tura_komputera()
        if len(reka_komputera) == 0:        # Wygrywa komputer
            koniec_partii = True
            print
            print u"Wygrał komputer!"
            # wyświetlamy wynik
            komp_punkty = 0
            for karta in reka_gracza:
                komp_punkty += karta.wartosc        # Dodajemy punkty z kart, jakie zostały na ręce gracza
            komp_razem += komp_punkty               # Dodajemy zdobyte punkty w tej partii, do sumarycznej liczby punktów
            print u"Komputer otrzymał %i punktów z kart na Twojej ręce" % komp_punkty
        if zablokowani >= 2:                        # Obaj grasz są zablokowani, więc oboje zdobywają punkty
            koniec_partii = True
            print u"Obaj zawodnicy są zablokowani. KONIEC GRY."
            gracz_punkty = 0
            for karta in reka_komputera:
                gracz_punkty += karta.wartosc
            gracz_razem += gracz_punkty
            komp_punkty = 0
            for karta in reka_gracza:
                komp_punkty += karta.wartosc
            komp_razem += komp_punkty
            # Wyświetlamy punkty zdobyte w partii
            print u"Otrzymałeś %i punktów z kart na ręce komptera" % gracz_punkty
            print u"Komputer otrzymał %i punktów z kart na Twojej ręce" % komp_punkty
    jeszcze_raz = raw_input("Jeszcze jedna partia (T/N)? ")
    if jeszcze_raz.lower().startswith('t'):
        koniec = False
        # Wyświetlamy całkowitą liczbę punktów
        print u"\nZdobyłeś do tej pory %i punktów" % gracz_razem
        print u"a komputer zdobył %i punktów.\n" % komp_razem
    else:
        koniec = True

# Wyświetlamy końcowy wynik
print u"\n Końcowy wynik:"
print "Ty: %i Komputer: %i" % (gracz_razem, komp_razem)

