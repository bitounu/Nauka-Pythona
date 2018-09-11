# Listing_13-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Próba modyfikacji zmiennej globalnej wewn¹trz funkcji

# definiujemy funkcjê obliczBrutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    mojaCenaNetto = 10000                                        # modyfikujemy zmienn¹ mojaCenaNetto wewn¹trz funkcji
    print "mojaCenaNetto (wewn¹trz funkcji) = ", mojaCenaNetto   # wyœwietlamy wartoœæ zmiennej lokalnej mojaCenaNetto
    return razem

# funkcjê wywo³ujemy w programie g³ównym
mojaCenaNetto = float(raw_input ("WprowadŸ cenê netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
print "mojaCenaNetto (na zewn¹trz funkcji) = ", mojaCenaNetto   # wyœwietlamy globaln¹ wersjê zmiennej mojaCenaNetto

