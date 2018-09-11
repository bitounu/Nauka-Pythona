# Listing_14-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z metody __str__() w celu zmiany sposobu wy�wietlania obiektu

class Pilka:
    def __init__(self, kolor, rozmiar, kierunek):
        self.kolor = kolor
        self.rozmiar = rozmiar
        self.kierunek = kierunek
        
    # tutaj znajduje si� metoda specjalna __str__()
    def __str__(self):
        komunikat = "Cze��, jestem " + self.rozmiar + " " + self.kolor + " pi�ka!"
        return komunikat
    
mojaPilka = Pilka("czerwona", "ma�a", "d�")
print mojaPilka

