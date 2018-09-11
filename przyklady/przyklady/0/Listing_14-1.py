# Listing_14-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Tworzenie prostej klasy Pilka

class Pilka:    # Tutaj wskazujemy Pythonowi, że tworzymy klasę

    def odbij(self):                # To jest metoda
        if self.kierunek == "dół":  #
            self.kierunek = "góra"  #
