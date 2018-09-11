# Listing_14-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z klasy Pilka

class Pilka:                                    # definicja klasy
                                                #
    def odbij(self):                            #
        if self.kierunek == "dół":              #
            self.kierunek = "góra"              #

mojaPilka = Pilka()                             # tworzymy instancję
mojaPilka.kierunek = "dół"                      # ustawiamy atrybuty
mojaPilka.kolor = "czerwona"                    #
mojaPilka.rozmiar = "mała"                      #

print "Właśnie utworzyłem piłkę."
print "Moja piłka jest", mojaPilka.rozmiar      # wyświetlają się atrybuty
print "Moja piłka jest", mojaPilka.kolor
print "Kierunek piłki to", mojaPilka.kierunek
print "Teraz piłka się odbije."
print
mojaPilka.odbij()                               # odbijamy piłkę
print "Teraz kierunek piłki to", mojaPilka.kierunek
