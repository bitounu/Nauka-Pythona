# Listing_11-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wyœwietlanie kilku tabliczek mno¿enia jednoczeœnie

for mnoznik in range (5, 8):                            # B
    for i in range (1, 11):                         # A # B 
        print i, "x", mnoznik, "=", i * mnoznik     # A # B
    print                                               # B


#A Wewnêtrzna pêtla wyœwietla jedn¹ tabliczkê mno¿enia
#B Zewnêtrza pêtla sk³ada siê z 3 iteracji i wartoœci licznika s¹ równe kolejno: 5, 6, 7
