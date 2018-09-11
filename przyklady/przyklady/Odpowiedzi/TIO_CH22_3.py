# TIO_CH22_3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 3, z rozdzia³u 22.

# Zapisujemy dane w pliku za pomoc¹ modu³u pickle

import pickle

imie = raw_input("Podaj swoje imiê: ")
wiek = raw_input("Podaj swój wiek: ")
kolor = raw_input("Podaj swój ulubiony kolor: ")
potrawa = raw_input("Podaj swoj¹ ulubion¹ potrawê: ")

moja_lista = [imie, wiek, kolor, potrawa]

plik = open("moj_plik.pkl", 'w')
pickle.dump(moja_lista, plik)

plik.close()

