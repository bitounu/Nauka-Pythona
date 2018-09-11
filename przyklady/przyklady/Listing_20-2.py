# Listing_20-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Dodajemy procedurê obs³ugi zdarzenia dla przycisku

import sys
from PyQt4 import QtCore, QtGui, uic

klasa_formularza = uic.loadUiType("MojPierwszyGui.ui")[0]

# Definicja klasy okna g³ównego
class KlasaMojeOkno(QtGui.QMainWindow, klasa_formularza):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.przycisk_klikniety)    # £¹czymy procedurê obs³ugi zdarzenia z okreœlonym zdarzeniem

    # Procedura obs³ugi zdarzenia dla przycisku
    def przycisk_klikniety(self):
        x = self.pushButton.x()
        y = self.pushButton.y()
        x += 50
        y += 50
        self.pushButton.move(x, y)  # Przesuwamy przycisk po klikniêciu na nim

app = QtGui.QApplication(sys.argv)
mojeOkno = KlasaMojeOkno()
mojeOkno.show()
app.exec_()
