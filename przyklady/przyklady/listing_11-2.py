# Listing_11-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Zmienna pêtla zagnie¿d¿ona

ileLinii = int(raw_input ('W ilu liniach maj¹ byæ wyœwietlone gwiazdki? '))
ileGwiazdek = int(raw_input ('Ile gwiazdek w linii? '))
for linia in range(0, ileLinii):
    for gwiazdka in range(0, ileGwiazdek):
        print '*',
    print

