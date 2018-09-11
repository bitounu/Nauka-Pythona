# Listing_23-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzenie talii kart

# Zwr�� uwag�, �e to nie jest kompletny program.  Aby utowrzy� kompletny program gry w Szalone �semki,
#   nale�y po��czy� poni�szy kod z pososta�ymi elemenatmi.

import random
from karty import Karta     # Importujemy modu� karty

# Tworzymy tali� za pomoc� zagnie�d�onej p�tli
talia = []
for kolor_id in range(1, 5):
    for figura_id in range(1, 14):
        talia.append(Karta(kolor_id, figura_id))

# Dobieramy na r�k� 5 kart z talii
reka = []
for karty in range(0, 5):
    a = random.choice(talia)
    reka.append(a)
    talia.remove(a)

print
for karta in reka:
    print karta.krotka_nazwa, '=' ,karta.dluga_nazwa, u" Warto��:", karta.wartosc
