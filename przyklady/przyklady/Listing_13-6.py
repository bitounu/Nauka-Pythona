# Listing_13-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# U�ycie zmiennej globalnej wewn�trz funkcji

# definiujemy funkcj� obliczBrutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    print mojaCenaNetto         # pr�ba wy�wietlenia warto�ci zmiennej mojaCenaNetto
    return razem

# funkcj� wywo�ujemy w programie g��wnym
mojaCenaNetto = float(raw_input ("Wprowad� cen� netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
