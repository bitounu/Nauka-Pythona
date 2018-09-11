#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------
# Zmień parametry aby uszyć własny szalik
#--------------------------------------------------

# kolory szalika
kolory = ['#','-','$']

# długość każdego koloru
dlugosc_koloru = 4

# długość szalika
dlugosc_szalika = 35

# szerokość szalika
szerokosc_szalika = 20

#------------------------------------------------
# Nie zmieniaj niczego poniżej tej linii!!!
#------------------------------------------------

print("Proszę bardzo, oto Twój szaliczek:\n")
for pos in range(int(szerokosc_szalika * dlugosc_szalika)):
    print( kolory[ int((pos)/dlugosc_koloru) % len(kolory)]),
    if (pos % szerokosc_szalika) == szerokosc_szalika-1:
        print("")
