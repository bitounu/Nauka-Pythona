# Listing_11-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Bardziej zawi³a wersja pêtli wyœwietlaj¹cej bloki gwiazdek

ileBlokow = int(raw_input('Ile bloków z gwiazdkami chcesz wyœwietliæ? '))
for blok in range(1, ileBlokow + 1):
    for linia in range(1, blok * 2 ):                   # Wzory obliczaj¹ce liczbê linii 
        for gwiazdka in range(1, (blok + linia) * 2):   # i gwiazdek
            print '*',
        print
    print


