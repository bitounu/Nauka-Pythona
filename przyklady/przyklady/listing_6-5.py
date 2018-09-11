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
easygui.msgbox("""AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadkę!
Jest nią tajemna liczba od 1 do 99. Na odgadnięcie jej masz 6 prób.""")

# Gracz ma do wykorzystania tylko 6 prób
while propozycja != sekret and proba < 6:
    propozycja = easygui.integerbox("Jaka to liczba?") # Pobranie propozycji gracza
    if propozycja < sekret:
        easygui.msgbox(str(propozycja) + " jest za mała, psubracie!")
    elif propozycja > sekret:
        easygui.msgbox(str(propozycja) + " jest za duża, szczurze lądowy!")
    proba = proba + 1 # Zwiększenie liczby prób

# Wyświetlenie komunikatu na końcu rozgrywki
if propozycja == sekret:
    easygui.msgbox("Stop! Udało Ci się! Odgadłeś moją tajemną liczbę!")
else:
    easygui.msgbox("Wykorzystałeś wszystkie próby! Powodzenia następnym razem, koleżko!  Tajemna liczba to " + str(sekret)) 



