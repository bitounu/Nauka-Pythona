# Listing_13-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pr�ba modyfikacji zmiennej globalnej wewn�trz funkcji

# definiujemy funkcj� obliczBrutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    mojaCenaNetto = 10000                                        # modyfikujemy zmienn� mojaCenaNetto wewn�trz funkcji
    print "mojaCenaNetto (wewn�trz funkcji) = ", mojaCenaNetto   # wy�wietlamy warto�� zmiennej lokalnej mojaCenaNetto
    return razem

# funkcj� wywo�ujemy w programie g��wnym
mojaCenaNetto = float(raw_input ("Wprowad� cen� netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
print "mojaCenaNetto (na zewn�trz funkcji) = ", mojaCenaNetto   # wy�wietlamy globaln� wersj� zmiennej mojaCenaNetto

