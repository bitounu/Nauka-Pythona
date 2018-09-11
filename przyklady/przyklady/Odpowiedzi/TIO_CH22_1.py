# TIO_CH22_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowiedü do zadania praktycznego 1, z rozdzia≥u 22.

# Program tworzπcy úmieszne zdania

import random

przydawki_plik = open("przydawki.txt", 'r')
przydawki = przydawki_plik.readline()
lista_przydawek = przydawki.split(',')
przydawki_plik.close()

podmioty_plik = open("podmioty.txt", 'r')
podmioty = podmioty_plik.readline()
lista_podmiotow = podmioty.split(',')
podmioty_plik.close()

orzeczenia_plik = open("orzeczenia.txt", 'r')
orzeczenia = orzeczenia_plik.readline()
lista_orzeczen = orzeczenia.split(',')
orzeczenia_plik.close()

okoliczniki_plik = open("okoliczniki.txt", 'r')
okoliczniki = okoliczniki_plik.readline()
lista_okolicznikow = okoliczniki.split(',')
okoliczniki_plik.close()

przydawka = random.choice(lista_przydawek)
podmiot = random.choice(lista_podmiotow)
orzeczenie = random.choice(lista_orzeczen)
okolicznik = random.choice(lista_okolicznikow)

print przydawka, podmiot, orzeczenie, okolicznik + '.'

