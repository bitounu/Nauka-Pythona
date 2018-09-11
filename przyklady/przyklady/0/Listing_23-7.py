# Listing_23-7.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone ósemki - wyświetlamy karty na ręce gracza

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

print u"\nTwoja ręka: ",
for karta in reka_gracza:
    print karta.krotka_nazwa,
print u" Wiodąca karta: ", karta_wiodaca.krotka_nazwa
if karta_wiodaca.figura == '8':
    print u" Wiodący kolor:", kolor_wiodacy

