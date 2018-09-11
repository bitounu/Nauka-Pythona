# Listing_1-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Gra w odgadywanie liczb z rozdzia³u 1.

import random
sekret = random.randint(1, 99) # Wybranie losowej liczby
propozycja = 0
proba = 0
print "AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadkê!"
print "Jest ni¹ tajemna liczba od 1 do 99. Na odgadniêcie jej masz 6 prób."

# Gracz ma do wykorzystania tylko 6 prób
while propozycja != sekret and proba < 6:
   propozycja = input("Jaka to liczba?") # Pobranie propozycji gracza
   if propozycja < sekret:
      print "Za ma³a, psubracie!"
   elif propozycja > sekret:
      print "Za du¿a, szczurze l¹dowy!"

   proba = proba + 1 # Zwiêkszenie liczby prób

# Wyœwietlenie komunikatu na koñcu rozgrywki
if propozycja == sekret:
   print "Stop! Uda³o Ci siê! Odgad³eœ moj¹ tajemn¹ liczbê!"
else:
   print "Wykorzysta³eœ wszystkie próby! Powodzenia nastêpnym razem, kole¿ko!"
   print "Tajemna liczba to", sekret

