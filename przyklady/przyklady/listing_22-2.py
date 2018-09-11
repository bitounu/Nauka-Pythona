# Listing_22-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Dwukrotne wywo³anie metody readline()

moj_plik = open('notatki.txt', 'r')
pierwsza_linia = moj_plik.readline()
druga_linia = moj_plik.readline()
print "pierwsza linia = ", pierwsza_linia 
print "druga linia = ", druga_linia 
moj_plik.close()
