# Listing_11-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Bloki z gwiazdkami w podw�jnie zagnie�d�onej p�tli

ileBlokow = int(raw_input ('Ile blok�w z gwiazdkami chcesz wy�wietli�? '))
ileLinii = int(raw_input ('Ile linii ma by� w ka�dym bloku? '))
ileGwiazdek = int(raw_input ('Ile gwiazdek w linii? '))
for blok in range(0, ileBlokow):
    for linia in range(0, ileLinii):
        for gwiazdka in range(0, ileGwiazdek):
            print '*',
        print
    print

