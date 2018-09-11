# Listing_22-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z trybu do³¹czania

do_zrobienia = open('notatki.txt', 'a') # Otwieramy plik w trybie do³¹czania
do_zrobienia.write('\nWydaæ kieszonkowe') # Dodajemy na koñcu nowy ³añcuch znakowy
do_zrobienia.close() # Zamykamy plik
