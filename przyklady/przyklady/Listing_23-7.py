# Listing_23-7.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone ósemki - wyœwietlamy karty na rêce gracza

# Zwróæ uwagê, ¿e to nie jest kompletny program.  Aby utowrzyæ kompletny program gry w Szalone ósemki,
#   nale¿y po³¹czyæ poni¿szy kod z pososta³ymi elemenatmi.

print u"\nTwoja rêka: ",
for karta in reka_gracza:
    print karta.krotka_nazwa,
print u" Wiod¹ca karta: ", karta_wiodaca.krotka_nazwa
if karta_wiodaca.figura == '8':
    print u" Wiod¹cy kolor:", kolor_wiodacy

