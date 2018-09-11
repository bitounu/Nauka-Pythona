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
        if self.kierunek == "dół":
            self.kierunek = "góra"

mojaPilka = Pilka("czerwona", "mała", "dół")        # tworzymy instancję i określamy atrybuty
print "Właśnie utworzyłem piłkę."
print "Moja piłka jest", mojaPilka.rozmiar
print "Moja piłka jest", mojaPilka.kolor
print "Kierunek piłki to", mojaPilka.kierunek
print "Teraz piłka się odbije."
print
mojaPilka.odbij()
print "Teraz kierunek piłki to", mojaPilka.kierunek

