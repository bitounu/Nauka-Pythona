# Listing_23-6.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# G³ówna pêtla programu Szalone ósemki

# Zwróæ uwagê, ¿e to nie jest kompletny program.  Aby utowrzyæ kompletny program gry w Szalone ósemki,
#   nale¿y po³¹czyæ poni¿szy kod z pososta³ymi elemenatmi.

inicjalizacja_kart()
while not koniec_partii:
    zablokowani = 0
    tura_gracza()
    if len(reka_gracza) == 0:       # Na rêce gracza nie ma ju¿ ¿adnych kart, wiêc wygrywa on partiê
        koniec_partii = True
        print
        print u"Wygra³eœ!"
    if not koniec_partii:
        tura_komputera()
    if len(reka_komputera) == 0:    # Na rêce komputera nie ma ju¿ ¿adnych kart, wiêc wygrywa on partiê
        koniec_partii = True
        print
        print u"Wygra³ komputer!"
    if zablokowani >= 2:        # Gracze s¹ zablokowani, wiêc koñczymy partiê
        koniec_partii = True
        print u"Gracze s¹ zablokowani. KONIEC GRY."
