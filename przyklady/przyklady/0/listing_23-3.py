# Listing_23-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Sprawdzamy ile razy wypadnie pod rząd 10 orzełków

from random import *
moneta = ["Orzelek", "Reszka"]
orzelki_z_rzedu = 0
dziesiec_orzelkow_z_rzedu = 0
for i in range (1000000):
    if choice(moneta) == "Orzelek":     # Rzucamy monetą
        orzelki_z_rzedu += 1
    else:
        orzelki_z_rzedu = 0
    if orzelki_z_rzedu == 10:
        dziesiec_orzelkow_z_rzedu += 1  # Wyrzuciliśmy 10 razy z rzędu orzełka, inkrementujemy licznik
        orzelki_z_rzedu = 0

print "10 orzełków z rzędu wyrzuciłem", dziesiec_orzelkow_z_rzedu, "razy."


