# Listing_23-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rzucamy 1000 razy dwiema koœæmi 6-œciennymi

import random

sumy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    kostka_1 = random.randint(1, 6)
    kostka_2 = random.randint(1, 6)
    suma_oczek = kostka_1 + kostka_2
    sumy[suma_oczek] += 1

for i in range(2, 13):
    print "suma", i, "oczek wypad³a",sumy[i], "razy"

