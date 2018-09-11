# Listing_22-1.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Otwieranie i odczytywanie pliku

moj_plik = open('notatki.txt', 'r')
linie = moj_plik.readlines()
print linie

