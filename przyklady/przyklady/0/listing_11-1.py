# Listing_11-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wyświetlanie kilku tabliczek mnożenia jednocześnie

for mnoznik in range (5, 8):                            # B
    for i in range (1, 11):                         # A # B 
        print i, "x", mnoznik, "=", i * mnoznik     # A # B
    print                                               # B


#A Wewnętrzna pętla wyświetla jedną tabliczkę mnożenia
#B Zewnętrza pętla składa się z 3 iteracji i wartości licznika są równe kolejno: 5, 6, 7
