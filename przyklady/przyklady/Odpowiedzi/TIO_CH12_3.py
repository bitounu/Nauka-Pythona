# TIO_CH12_3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 3, z rozdzia³u 12.

listaImion = []
print "WprowadŸ piêæ imion (po ka¿dym z nich naciœnij Enter):"
for i in range(5):
    imie = raw_input()
    listaImion.append(imie)

print "Trzecie imiê to:", listaImion[2]
