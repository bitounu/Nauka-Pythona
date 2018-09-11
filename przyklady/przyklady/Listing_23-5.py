# Listing_23-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzenie talii kart

# Zwróæ uwagê, ¿e to nie jest kompletny program.  Aby utowrzyæ kompletny program gry w Szalone ósemki,
#   nale¿y po³¹czyæ poni¿szy kod z pososta³ymi elemenatmi.

import random
from karty import Karta     # Importujemy modu³ karty

# Tworzymy taliê za pomoc¹ zagnie¿d¿onej pêtli
talia = []
for kolor_id in range(1, 5):
    for figura_id in range(1, 14):
        talia.append(Karta(kolor_id, figura_id))

# Dobieramy na rêkê 5 kart z talii
reka = []
for karty in range(0, 5):
    a = random.choice(talia)
    reka.append(a)
    talia.remove(a)

print
for karta in reka:
    print karta.krotka_nazwa, '=' ,karta.dluga_nazwa, u" Wartoœæ:", karta.wartosc
