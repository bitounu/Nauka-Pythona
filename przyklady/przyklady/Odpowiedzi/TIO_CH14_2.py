# TIO_CH14_2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 2, z rozdzia�u 14.

class RachunekBankowy:
    def __init__(self, numer_rachunku, nazwa_rachunku):
        self.numer_rachunku = numer_rachunku
        self.nazwa_rachunku = nazwa_rachunku
        self.saldo = 0.0

    def wyswietlSaldo(self):
        print "Saldo wynosi:", self.saldo

    def wplata(self, kwota):
        self.saldo = self.saldo + kwota
        print "Wp�aci�e�", kwota
        print "Saldo wynosi teraz:", self.saldo

    def podjecie(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota
            print "Podj��e�", kwota
            print "Saldo wynosi teraz:", self.saldo
        else:
            print "Pr�bowa�e� podj�� kwot�", kwota
            print "Saldo wynosi:", self.saldo
            print "Odmowa wyp�acenia pieni�dzy. Brak �rodk�w na rachunku."
    
class RachunekOszczednosciowy(RachunekBankowy):
    def __init__(self, numer_rachunku, nazwa_rachunku, oprocentowanie):
        RachunekBankowy.__init__(self, numer_rachunku, nazwa_rachunku)
        self.oprocentowanie = oprocentowanie
    def dodajOdsetki(self):
        odsetki = self.saldo * self.oprocentowanie
        print "dodaj� odsetki w wysoko�ci,", self.oprocentowanie * 100, "procent"
        self.wplata(odsetki)


mojRachunek = RachunekBankowy(234567, "Warren Sande", 0.11)
print "Nazwa rachunku:", mojRachunek.numer_rachunku
print "Numer rachunku:", mojRachunek.nazwa_rachunku
mojRachunek.wyswietlSaldo()
mojRachunek.wplata(34.52)
mojRachunek.dodajOdsetki()
