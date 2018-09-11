# Listing_20-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Program do konwertowania temperatury

import sys
from PyQt4 import QtCore, QtGui, uic

klasa_formularza = uic.loadUiType("tempkonwer.ui")[0]   # £adujemy UI programu do konwertowania temperatury 

class KlasaMojeOkno(QtGui.QMainWindow, klasa_formularza):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCnaF.clicked.connect(self.btnCnaF_klikniety)    # przypisujemy do przycisków
        self.btnFnaC.clicked.connect(self.btnFnaC_klikniety)    # procedury obs³ugi zdarzenia

    def btnCnaF_klikniety(self):                    # procedura obs³ugi zdarzenia dla przycisku btnCnaF
        cel = float(self.editCel.text())            #
        fahr = cel * 9.0 / 5 + 32                   #
        self.spinFahr.setValue(int(fahr + 0.5))     #

    def btnFnaC_klikniety(self):                    # procedura obs³ugi zdarzenia dla przycisku btnFnaC
        fahr = self.spinFahr.value()                #
        cel = (fahr - 32) * 5.0 / 9                 #
        self.editCel.setText(str(cel))              #

app = QtGui.QApplication(sys.argv)
mojeOkno = KlasaMojeOkno()
mojeOkno.show()
app.exec_()

