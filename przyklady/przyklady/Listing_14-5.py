# Listing_14-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pocz�tkowa wersja programu z hot dogiem

class HotDog:
    def __init__(self):
        self.podgrzanie_poziom = 0
        self.podgrzanie_tekst = "Surowy"
        self.dodatki = []
        
    def podgrzej(self, czas):
        # zwi�kszenie poziomu podgrzania o okre�lony czas
        self.podgrzanie_poziom = self.podgrzanie_poziom + czas
        # ustawienie �a�cuch�w znakowych w zale�no�ci od poziomu podgrzania
        if self.podgrzanie_poziom > 8:
            self.podgrzanie_tekst = "Spalony"
        elif self.podgrzanie_poziom > 5:
            self.podgrzanie_tekst = "Mocno podgrzany"
        elif self.podgrzanie_poziom > 3:
            self.podgrzanie_tekst = "�rednio podgrzany"
        else:
            self.podgrzanie_tekst = "Surowy"
            
mojHotDog = HotDog()        # tworzymy instancj�

print mojHotDog.podgrzanie_poziom
print mojHotDog.podgrzanie_tekst
print mojHotDog.dodatki
