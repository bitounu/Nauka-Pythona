# Listing_22-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z trybu dołączania

do_zrobienia = open('notatki.txt', 'a') # Otwieramy plik w trybie dołączania
do_zrobienia.write('\nWydać kieszonkowe') # Dodajemy na końcu nowy łańcuch znakowy
do_zrobienia.close() # Zamykamy plik
