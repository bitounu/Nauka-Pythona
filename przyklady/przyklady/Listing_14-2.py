# Listing_14-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z klasy Pilka

class Pilka:                                    # definicja klasy
                                                #
    def odbij(self):                            #
        if self.kierunek == "dó³":              #
            self.kierunek = "góra"              #

mojaPilka = Pilka()                             # tworzymy instancjê
mojaPilka.kierunek = "dó³"                      # ustawiamy atrybuty
mojaPilka.kolor = "czerwona"                    #
mojaPilka.rozmiar = "ma³a"                      #

print "W³aœnie utworzy³em pi³kê."
print "Moja pi³ka jest", mojaPilka.rozmiar      # wyœwietlaj¹ siê atrybuty
print "Moja pi³ka jest", mojaPilka.kolor
print "Kierunek pi³ki to", mojaPilka.kierunek
print "Teraz pi³ka siê odbije."
print
mojaPilka.odbij()                               # odbijamy pi³kê
print "Teraz kierunek pi³ki to", mojaPilka.kierunek
