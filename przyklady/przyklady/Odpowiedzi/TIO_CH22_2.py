# TIO_CH22_2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 2, z rozdzia�u 22.

# Zapisujemy dane w pliku tekstowym

imie = raw_input("Podaj swoje imi�: ")
wiek = raw_input("Podaj sw�j wiek: ")
kolor = raw_input("Podaj sw�j ulubiony kolor: ")
potrawa = raw_input("Podaj swoj� ulubion� potraw�: ")

moje_dane = open("moje_dane_plik.txt", 'w')
moje_dane.write(imie + "\n")
moje_dane.write(wiek + "\n")
moje_dane.write(kolor + "\n")
moje_dane.write(potrawa)

moje_dane.close()
