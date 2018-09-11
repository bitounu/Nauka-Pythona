# -*- coding: utf-8 -*-
# Listing_23-9.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone Ăłsemki - wybieranie nowego koloru, kiedy gracz zagra kartÄ™ 8

# ZwrĂłÄ‡ uwagÄ™, ĹĽe to nie jest kompletny program.  Aby utowrzyÄ‡ kompletny program gry w Szalone Ăłsemki,
#   naleĹĽy poĹ‚Ä…czyÄ‡ poniĹĽszy kod z posostaĹ‚ymi elemenatmi.

def pobierz_nowy_kolor():
    global kolor_wiodacy
    kolor_wybrany = False
    while not kolor_wybrany:    # Wykonujemy pÄ™tlÄ™, dopĂłki gracz nie wprowadzi prawidĹ‚owej karty 
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
            kolor_wiodacy = u"ZoĹ‚Ä™dzie"
            kolor_wybrany = True
        else:
            print u"NieprawidĹ‚owy kolor. SprĂłbuj ponownie. ",
    print u"WybraĹ‚eĹ›", kolor_wiodacy
