# Listing_13-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Użycie zmiennej globalnej wewnątrz funkcji

# definiujemy funkcję obliczBrutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    print mojaCenaNetto         # próba wyświetlenia wartości zmiennej mojaCenaNetto
    return razem

# funkcję wywołujemy w programie głównym
mojaCenaNetto = float(raw_input ("Wprowadź cenę netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
