# Listing_13-4
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzenie oraz stosowanie funkcji, która zwraca wartość

# Funkcja oblicza podatek i zwraca cenę brutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    return razem                    # Zwrócenie wyniku do programu głównego

mojaCenaNetto = float(raw_input ("Wprowadź cenę netto: "))

# Wywołanie funkcji i zapisanie wyniku w zmiennej 
cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)

print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
