# Listing_14-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z klasy Pilka

class Pilka:                                    # definicja klasy
                                                #
    def odbij(self):                            #
        if self.kierunek == "d�":              #
            self.kierunek = "g�ra"              #

mojaPilka = Pilka()                             # tworzymy instancj�
mojaPilka.kierunek = "d�"                      # ustawiamy atrybuty
mojaPilka.kolor = "czerwona"                    #
mojaPilka.rozmiar = "ma�a"                      #

print "W�a�nie utworzy�em pi�k�."
print "Moja pi�ka jest", mojaPilka.rozmiar      # wy�wietlaj� si� atrybuty
print "Moja pi�ka jest", mojaPilka.kolor
print "Kierunek pi�ki to", mojaPilka.kierunek
print "Teraz pi�ka si� odbije."
print
mojaPilka.odbij()                               # odbijamy pi�k�
print "Teraz kierunek pi�ki to", mojaPilka.kierunek
