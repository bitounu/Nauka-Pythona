# Listing_22-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Otwieranie istniej¹cego pliku w trybie do zapisu

plik = open('notatki.txt', 'w')
plik.write("Wstaæ z ³ó¿ka\n")
plik.write("Obejrzeæ kreskówki")
plik.close()

