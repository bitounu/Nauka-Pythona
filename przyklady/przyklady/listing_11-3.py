# Listing_11-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Bloki z gwiazdkami w podwójnie zagnie¿d¿onej pêtli

ileBlokow = int(raw_input ('Ile bloków z gwiazdkami chcesz wyœwietliæ? '))
ileLinii = int(raw_input ('Ile linii ma byæ w ka¿dym bloku? '))
ileGwiazdek = int(raw_input ('Ile gwiazdek w linii? '))
for blok in range(0, ileBlokow):
    for linia in range(0, ileLinii):
        for gwiazdka in range(0, ileGwiazdek):
            print '*',
        print
    print

