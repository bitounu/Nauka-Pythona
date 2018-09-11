# -*- coding: utf-8 -*-
# Listing_6-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Number Guess game using EasyGui

import random, easygui
sekret = random.randint(1, 99) # Wybranie losowej liczby
propozycja = 0
proba = 0
easygui.msgbox("""AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadkÄ™!
Jest niÄ… tajemna liczba od 1 do 99. Na odgadniÄ™cie jej masz 6 prĂłb.""")

# Gracz ma do wykorzystania tylko 6 prĂłb
while propozycja != sekret and proba < 6:
    propozycja = easygui.integerbox("Jaka to liczba?") # Pobranie propozycji gracza
    if propozycja < sekret:
        easygui.msgbox(str(propozycja) + " jest za maĹ‚a, psubracie!")
    elif propozycja > sekret:
        easygui.msgbox(str(propozycja) + " jest za duĹĽa, szczurze lÄ…dowy!")
    proba = proba + 1 # ZwiÄ™kszenie liczby prĂłb

# WyĹ›wietlenie komunikatu na koĹ„cu rozgrywki
if propozycja == sekret:
    easygui.msgbox("Stop! UdaĹ‚o Ci siÄ™! OdgadĹ‚eĹ› mojÄ… tajemnÄ… liczbÄ™!")
else:
    easygui.msgbox("WykorzystaĹ‚eĹ› wszystkie prĂłby! Powodzenia nastÄ™pnym razem, koleĹĽko!  Tajemna liczba to " + str(sekret)) 



