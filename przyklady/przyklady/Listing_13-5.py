# Listing_13-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Próba wyœwietlenia zmiennej lokalnej

# Funkcja oblicza podatek i zwraca cenê brutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    return razem

mojaCenaNetto = float(raw_input ("WprowadŸ cenê netto: "))

# Wywo³anie funkcji i zapisanie wyniku w zmiennej 
cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
print cenaNetto
