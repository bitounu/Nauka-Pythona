# Listing_13-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# U¿ycie zmiennej globalnej wewn¹trz funkcji

# definiujemy funkcjê obliczBrutto
def obliczBrutto(cenaNetto, stawka_podatku):
    razem = cenaNetto + (cenaNetto * stawka_podatku)
    print mojaCenaNetto         # próba wyœwietlenia wartoœci zmiennej mojaCenaNetto
    return razem

# funkcjê wywo³ujemy w programie g³ównym
mojaCenaNetto = float(raw_input ("WprowadŸ cenê netto: "))

cenaBrutto = obliczBrutto(mojaCenaNetto, 0.23)
print "Cena netto = ", mojaCenaNetto, " Cena brutto = ", cenaBrutto
