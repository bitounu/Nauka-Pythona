# Listing_23-6.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# G��wna p�tla programu Szalone �semki

# Zwr�� uwag�, �e to nie jest kompletny program.  Aby utowrzy� kompletny program gry w Szalone �semki,
#   nale�y po��czy� poni�szy kod z pososta�ymi elemenatmi.

inicjalizacja_kart()
while not koniec_partii:
    zablokowani = 0
    tura_gracza()
    if len(reka_gracza) == 0:       # Na r�ce gracza nie ma ju� �adnych kart, wi�c wygrywa on parti�
        koniec_partii = True
        print
        print u"Wygra�e�!"
    if not koniec_partii:
        tura_komputera()
    if len(reka_komputera) == 0:    # Na r�ce komputera nie ma ju� �adnych kart, wi�c wygrywa on parti�
        koniec_partii = True
        print
        print u"Wygra� komputer!"
    if zablokowani >= 2:        # Gracze s� zablokowani, wi�c ko�czymy parti�
        koniec_partii = True
        print u"Gracze s� zablokowani. KONIEC GRY."
