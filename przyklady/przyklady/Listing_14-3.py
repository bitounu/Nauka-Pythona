# Listing_14-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z metody __init__()

class Pilka:
    def __init__(self, kolor, rozmiar, kierunek):   # to jest metoda __init__()
        self.kolor = kolor                          #
        self.rozmiar = rozmiar                      #
        self.kierunek = kierunek                    #

    def odbij(self):
        if self.kierunek == "dó³":
            self.kierunek = "góra"

mojaPilka = Pilka("czerwona", "ma³a", "dó³")        # tworzymy instancjê i okreœlamy atrybuty
print "W³aœnie utworzy³em pi³kê."
print "Moja pi³ka jest", mojaPilka.rozmiar
print "Moja pi³ka jest", mojaPilka.kolor
print "Kierunek pi³ki to", mojaPilka.kierunek
print "Teraz pi³ka siê odbije."
print
mojaPilka.odbij()
print "Teraz kierunek pi³ki to", mojaPilka.kierunek

