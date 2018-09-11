# Listing_22-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Otwieranie istniejącego pliku w trybie do zapisu

plik = open('notatki.txt', 'w')
plik.write("Wstać z łóżka\n")
plik.write("Obejrzeć kreskówki")
plik.close()

