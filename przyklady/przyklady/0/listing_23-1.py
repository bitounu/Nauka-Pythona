# Listing_23-1.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rzucamy 1000 razy jedną kością 11-ścienną

import random

sumy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      # Lista zawiera 13 elementów o indeksach od 0 do 12
for i in range(1000):
    suma_oczek = random.randint(2, 12)
    sumy[suma_oczek] += 1                           # Zwiększamy o 1 krotność wyrzuconej liczby oczek

for i in range(2, 13):
    print "suma", i, "oczek wypadła",sumy[i], "razy"
