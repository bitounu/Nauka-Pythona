# Gra w odgadywanie liczb z rozdziału 1.

import random
sekret = random.randint(1, 99) # Wybranie losowej liczby
propozycja = 0
proba = 0
print "AHOJ! Jam jest pirat Roberts Straszliwy i mam dla Ciebie zagadkę!"
print "Jest nią tajemna liczba od 1 do 99. Na odgadnięcie jej masz 6 prób."

# Gracz ma do wykorzystania tylko 6 prób
while propozycja != sekret and proba < 6:
   propozycja = input("Jaka to liczba?") # Pobranie propozycji gracza
   if propozycja < sekret:
      print "Za mała, psubracie!"
   elif propozycja > sekret:
      print "Za duża, szczurze lądowy!"

   proba = proba + 1 # Zwiększenie liczby prób

# Wyświetlenie komunikatu na końcu rozgrywki
if propozycja == sekret:
   print "Stop! Udało Ci się! Odgadłeś moją tajemną liczbę!"
else:
   print "Wykorzystałeś wszystkie próby! Powodzenia następnym razem, koleżko!"
   print "Tajemna liczba to", sekret
