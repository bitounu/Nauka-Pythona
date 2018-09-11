# Listing_23-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Sprawdzamy ile razy wypadnie pod rz¹d 10 orze³ków

from random import *
moneta = ["Orzelek", "Reszka"]
orzelki_z_rzedu = 0
dziesiec_orzelkow_z_rzedu = 0
for i in range (1000000):
    if choice(moneta) == "Orzelek":     # Rzucamy monet¹
        orzelki_z_rzedu += 1
    else:
        orzelki_z_rzedu = 0
    if orzelki_z_rzedu == 10:
        dziesiec_orzelkow_z_rzedu += 1  # Wyrzuciliœmy 10 razy z rzêdu orze³ka, inkrementujemy licznik
        orzelki_z_rzedu = 0

print "10 orze³ków z rzêdu wyrzuci³em", dziesiec_orzelkow_z_rzedu, "razy."


