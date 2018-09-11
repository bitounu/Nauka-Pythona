# Listing_14-5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Początkowa wersja programu z hot dogiem

class HotDog:
    def __init__(self):
        self.podgrzanie_poziom = 0
        self.podgrzanie_tekst = "Surowy"
        self.dodatki = []
        
    def podgrzej(self, czas):
        # zwiększenie poziomu podgrzania o określony czas
        self.podgrzanie_poziom = self.podgrzanie_poziom + czas
        # ustawienie łańcuchów znakowych w zależności od poziomu podgrzania
        if self.podgrzanie_poziom > 8:
            self.podgrzanie_tekst = "Spalony"
        elif self.podgrzanie_poziom > 5:
            self.podgrzanie_tekst = "Mocno podgrzany"
        elif self.podgrzanie_poziom > 3:
            self.podgrzanie_tekst = "Średnio podgrzany"
        else:
            self.podgrzanie_tekst = "Surowy"
            
mojHotDog = HotDog()        # tworzymy instancję

print mojHotDog.podgrzanie_poziom
print mojHotDog.podgrzanie_tekst
print mojHotDog.dodatki
