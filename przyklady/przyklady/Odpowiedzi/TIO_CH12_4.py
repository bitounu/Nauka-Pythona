# TIO_CH12_4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 4, z rozdzia�u 12.

listaImion = []
print "Wprowad� pi�� imion (po ka�dym z nich naci�nij Enter):"
for i in range(5):
    imie = raw_input()
    listaImion.append(imie)
    
print "Oto imiona:", listaImion
print "Zamie� jedno z imion. Kt�re? (1-5):",
zamien = int(raw_input())
nowe = raw_input("Nowe imi�: ")
listaImion[zamien - 1] = nowe
print "Oto imiona:", listaImion


