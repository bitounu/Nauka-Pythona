# Listing_23-1.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rzucamy 1000 razy jedn� ko�ci� 11-�cienn�

import random

sumy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      # Lista zawiera 13 element�w o indeksach od 0 do 12
for i in range(1000):
    suma_oczek = random.randint(2, 12)
    sumy[suma_oczek] += 1                           # Zwi�kszamy o 1 krotno�� wyrzuconej liczby oczek

for i in range(2, 13):
    print "suma", i, "oczek wypad�a",sumy[i], "razy"
