# -*- coding: utf-8 -*-
# Listing_23-9.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone ósemki - wybieranie nowego koloru, kiedy gracz zagra kartę 8

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

def pobierz_nowy_kolor():
    global kolor_wiodacy
    kolor_wybrany = False
    while not kolor_wybrany:    # Wykonujemy pętlę, dopóki gracz nie wprowadzi prawidłowej karty 
        kolor = raw_input("Wybierz kolor: ")
        if kolor.lower() == 'd':
            kolor_wiodacy = "Dzwonki"
            kolor_wybrany = True
        elif kolor.lower() == 'w':
            kolor_wiodacy = "Wino"
            kolor_wybrany = True
        elif kolor.lower() == 's':
            kolor_wiodacy = "Serce"
            kolor_wybrany = True
        elif kolor.lower() == 'z':
            kolor_wiodacy = u"Zołędzie"
            kolor_wybrany = True
        else:
            print u"Nieprawidłowy kolor. Spróbuj ponownie. ",
    print u"Wybrałeś", kolor_wiodacy
