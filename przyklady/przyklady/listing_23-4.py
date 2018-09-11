# Listing_23-4.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Klasa s�u��ca do gry w karty
#  (Uwaga: ten listing nie jest kompletnym programem, kt�ry mo�na uruchomi�)
#   Jest to modu�, kt�ry zaimportujemy w innym programie.)

class Karta:
    def __init__(self, kolor_id, figura_id):
        self.figura_id = figura_id
        self.kolor_id = kolor_id

        # Tworzymy atrybuty figura i wartosc
        if self.figura_id == 1:
            self.figura = "As"
            self.wartosc = 1
        elif self.figura_id == 11:
            self.figura = "Walet"
            self.wartosc = 10
        elif self.figura_id == 12:
            self.figura = "Dama"
            self.wartosc = 10
        elif self.figura_id == 13:
            self.figura = u"Kr�l"
            self.wartosc = 10
        elif 2 <= self.figura_id <= 10:
            self.figura = str(self.figura_id)
            self.wartosc = self.figura_id
        else:
            self.figura = u"B��dnaFigura"   # Sprawdzamy, czy wyst�pi� b��d
            self.wartosc = -1

        # Tworzymy atrybut kolor
        if self.kolor_id == 1:
            self.kolor = "Dzwonki"
        elif self.kolor_id == 2:
            self.kolor = "Serce"
        elif self.kolor_id == 3:
            self.kolor = "Wino"
        elif self.kolor_id == 4:
            self.kolor = u"Zo��dzie"
        else:
            self.kolor = u"B��dnyKolor"     # Sprawdzamy, czy wyst�pi� b��d
        self.krotka_nazwa = self.figura[0] + self.kolor[0]
        if self.figura == '10':
            self.krotka_nazwa = self.figura + self.kolor[0]
        self.dluga_nazwa = self.figura + " - " + self.kolor

