# Listing_23-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Sprawdzamy ile razy wypadnie pod rz�d 10 orze�k�w

from random import *
moneta = ["Orzelek", "Reszka"]
orzelki_z_rzedu = 0
dziesiec_orzelkow_z_rzedu = 0
for i in range (1000000):
    if choice(moneta) == "Orzelek":     # Rzucamy monet�
        orzelki_z_rzedu += 1
    else:
        orzelki_z_rzedu = 0
    if orzelki_z_rzedu == 10:
        dziesiec_orzelkow_z_rzedu += 1  # Wyrzucili�my 10 razy z rz�du orze�ka, inkrementujemy licznik
        orzelki_z_rzedu = 0

print "10 orze�k�w z rz�du wyrzuci�em", dziesiec_orzelkow_z_rzedu, "razy."


