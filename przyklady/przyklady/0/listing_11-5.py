# Listing_11-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wyświetlanie wartości zmiennych w pętli zagnieżdżonej

ileBlokow = int(raw_input('Ile bloków z gwiazdkami chcesz wyświetlić? '))
for blok in range(1, ileBlokow + 1):
    print 'blok = ', bool                                   # wyświetlamy zmienne
    for linia in range(1, blok * 2 ):
        for gwiazdka in range(1, (blok + linia) * 2):
            print '*',
        print ' linia = ', linia, 'gwiazdka = ', gwiazdka   # wyświetlamy zmienne
    print


