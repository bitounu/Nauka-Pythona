# Listing_11-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wyœwietlanie wartoœci zmiennych w pêtli zagnie¿d¿onej

ileBlokow = int(raw_input('Ile bloków z gwiazdkami chcesz wyœwietliæ? '))
for blok in range(1, ileBlokow + 1):
    print 'blok = ', bool                                   # wyœwietlamy zmienne
    for linia in range(1, blok * 2 ):
        for gwiazdka in range(1, (blok + linia) * 2):
            print '*',
        print ' linia = ', linia, 'gwiazdka = ', gwiazdka   # wyœwietlamy zmienne
    print


