# Listing_23-7.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone �semki - wy�wietlamy karty na r�ce gracza

# Zwr�� uwag�, �e to nie jest kompletny program.  Aby utowrzy� kompletny program gry w Szalone �semki,
#   nale�y po��czy� poni�szy kod z pososta�ymi elemenatmi.

print u"\nTwoja r�ka: ",
for karta in reka_gracza:
    print karta.krotka_nazwa,
print u" Wiod�ca karta: ", karta_wiodaca.krotka_nazwa
if karta_wiodaca.figura == '8':
    print u" Wiod�cy kolor:", kolor_wiodacy

