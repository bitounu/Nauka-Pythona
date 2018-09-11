# Listing_20-1.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Najbardziej podstawowy kod PyQt

import sys
from PyQt4 import QtCore, QtGui, uic    # Importujemy wymagane biblioteki PyQt

klasa_formularza = uic.loadUiType("MojPierwszyGui.ui")[0] # £adujemy UI utworzone wczeœniej w Qt Designerze 

class KlasaMojeOkno(QtGui.QMainWindow, klasa_formularza):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)  # Program PtQt, który wyœwietla okno
mojeOkno = KlasaMojeOkno()          # Tworzymy instancjê klasy okna
mojeOkno.show()                     # Uruchamiamy program 
app.exec_()                         # i wyœwietlamy GUI
