# Listing_11-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wy�wietlanie warto�ci zmiennych w p�tli zagnie�d�onej

ileBlokow = int(raw_input('Ile blok�w z gwiazdkami chcesz wy�wietli�? '))
for blok in range(1, ileBlokow + 1):
    print 'blok = ', bool                                   # wy�wietlamy zmienne
    for linia in range(1, blok * 2 ):
        for gwiazdka in range(1, (blok + linia) * 2):
            print '*',
        print ' linia = ', linia, 'gwiazdka = ', gwiazdka   # wy�wietlamy zmienne
    print


