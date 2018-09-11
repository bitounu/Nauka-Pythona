# TIO_CH12_4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 4, z rozdzia³u 12.

listaImion = []
print "WprowadŸ piêæ imion (po ka¿dym z nich naciœnij Enter):"
for i in range(5):
    imie = raw_input()
    listaImion.append(imie)
    
print "Oto imiona:", listaImion
print "Zamieñ jedno z imion. Które? (1-5):",
zamien = int(raw_input())
nowe = raw_input("Nowe imiê: ")
listaImion[zamien - 1] = nowe
print "Oto imiona:", listaImion


