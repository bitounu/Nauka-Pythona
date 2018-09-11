# Listing_23-5.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzenie talii kart

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

import random
from karty import Karta     # Importujemy moduł karty

# Tworzymy talię za pomocą zagnieżdżonej pętli
talia = []
for kolor_id in range(1, 5):
    for figura_id in range(1, 14):
        talia.append(Karta(kolor_id, figura_id))

# Dobieramy na rękę 5 kart z talii
reka = []
for karty in range(0, 5):
    a = random.choice(talia)
    reka.append(a)
    talia.remove(a)

print
for karta in reka:
    print karta.krotka_nazwa, '=' ,karta.dluga_nazwa, u" Wartość:", karta.wartosc
