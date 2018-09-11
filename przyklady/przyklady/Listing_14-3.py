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
        if self.kierunek == "d�":
            self.kierunek = "g�ra"

mojaPilka = Pilka("czerwona", "ma�a", "d�")        # tworzymy instancj� i okre�lamy atrybuty
print "W�a�nie utworzy�em pi�k�."
print "Moja pi�ka jest", mojaPilka.rozmiar
print "Moja pi�ka jest", mojaPilka.kolor
print "Kierunek pi�ki to", mojaPilka.kierunek
print "Teraz pi�ka si� odbije."
print
mojaPilka.odbij()
print "Teraz kierunek pi�ki to", mojaPilka.kierunek

