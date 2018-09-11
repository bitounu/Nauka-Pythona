# Listing_22-4.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Zapisujemy dane w nowym pliku

nowy_plik = open("nowe_notatki.txt", 'w')
nowy_plik.write("Zjeść kolację\n")
nowy_plik.write("Zagrać w piłkę\n")
nowy_plik.write("Pójść spać")
nowy_plik.close()

