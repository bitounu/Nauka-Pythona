# Listing_13-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Próba modyfikacji zmiennej globalnej wewnątrz funkcji

# definiujemy funkcję obliczBrutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    mojaCenaNetto = 10000                                        # modyfikujemy zmienną mojaCenaNetto wewnątrz funkcji
    print "mojaCenaNetto (wewnątrz funkcji) = ", mojaCenaNetto   # wyświetlamy wartość zmiennej lokalnej mojaCenaNetto
    return razem

# funkcję wywołujemy w programie głównym
mojaCenaNetto = float(raw_input ("Wprowadź cenę netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
print "mojaCenaNetto (na zewnątrz funkcji) = ", mojaCenaNetto   # wyświetlamy globalną wersję zmiennej mojaCenaNetto

