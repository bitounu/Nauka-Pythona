# TIO_CH14_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 1, z rozdzia³u 14.

class RachunekBankowy:
    def __init__(self, numer_rachunku, nazwa_rachunku):
        self.numer_rachunku = numer_rachunku
        self.nazwa_rachunku = nazwa_rachunku
        self.saldo = 0.0

    def wyswietlSaldo(self):
        print "Saldo wynosi:", self.saldo

    def wplata(self, kwota):
        self.saldo = self.saldo + kwota
        print "Wp³aci³eœ", kwota
        print "Saldo wynosi teraz:", self.saldo

    def podjecie(self, kwota):
        if self.saldo >= kwota:
            self.saldo = self.saldo - kwota
            print "Podj¹³eœ", kwota
            print "Saldo wynosi teraz:", self.saldo
        else:
            print "Próbowa³eœ podj¹æ kwotê", kwota
            print "Saldo wynosi:", self.saldo
            print "Odmowa wyp³acenia pieniêdzy. Brak œrodków na rachunku."


mojRachunek = RachunekBankowy(234567, "Warren Sande")
print "Nazwa rachunku:", mojRachunek.numer_rachunku
print "Numer rachunku:", mojRachunek.nazwa_rachunku
mojRachunek.wyswietlSaldo()

mojRachunek.wplata(34.52)
mojRachunek.podjecie(12.25)
mojRachunek.podjecie(30.18)



    
