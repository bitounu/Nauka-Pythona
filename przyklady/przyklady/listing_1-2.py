# Listing_1-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Gra w odgadywanie liczb z rozdzia�u 1.

import random
sekret = random.randint(1, 99) # Wybranie losowej liczby
propozycja = 0
proba = 0
print "AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadk�!"
print "Jest ni� tajemna liczba od 1 do 99. Na odgadni�cie jej masz 6 pr�b."

# Gracz ma do wykorzystania tylko 6 pr�b
while propozycja != sekret and proba < 6:
   propozycja = input("Jaka to liczba?") # Pobranie propozycji gracza
   if propozycja < sekret:
      print "Za ma�a, psubracie!"
   elif propozycja > sekret:
      print "Za du�a, szczurze l�dowy!"

   proba = proba + 1 # Zwi�kszenie liczby pr�b

# Wy�wietlenie komunikatu na ko�cu rozgrywki
if propozycja == sekret:
   print "Stop! Uda�o Ci si�! Odgad�e� moj� tajemn� liczb�!"
else:
   print "Wykorzysta�e� wszystkie pr�by! Powodzenia nast�pnym razem, kole�ko!"
   print "Tajemna liczba to", sekret

