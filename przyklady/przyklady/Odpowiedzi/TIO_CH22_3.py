# TIO_CH22_3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 3, z rozdzia�u 22.

# Zapisujemy dane w pliku za pomoc� modu�u pickle

import pickle

imie = raw_input("Podaj swoje imi�: ")
wiek = raw_input("Podaj sw�j wiek: ")
kolor = raw_input("Podaj sw�j ulubiony kolor: ")
potrawa = raw_input("Podaj swoj� ulubion� potraw�: ")

moja_lista = [imie, wiek, kolor, potrawa]

plik = open("moj_plik.pkl", 'w')
pickle.dump(moja_lista, plik)

plik.close()

