# Listing_11-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wy�wietlanie kilku tabliczek mno�enia jednocze�nie

for mnoznik in range (5, 8):                            # B
    for i in range (1, 11):                         # A # B 
        print i, "x", mnoznik, "=", i * mnoznik     # A # B
    print                                               # B


#A Wewn�trzna p�tla wy�wietla jedn� tabliczk� mno�enia
#B Zewn�trza p�tla sk�ada si� z 3 iteracji i warto�ci licznika s� r�wne kolejno: 5, 6, 7
