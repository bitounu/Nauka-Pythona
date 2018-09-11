# -*- coding: utf-8 -*-
# TIO_CH20-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowiedź do zadania praktycznego 1, z rozdziału 20.

# Gra w odgadywanie liczby w PyQt

import sys
from PyQt4 import QtCore, QtGui, uic
import random

klasa_formularza = uic.loadUiType("TIO_CH20_1.ui")[0]    # Ładujemy UI

propozycja = 0
sekret = random.randint(1, 100)
proby = 6

class MojaKlasaOkna(QtGui.QMainWindow, klasa_formularza):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnSprawdz.clicked.connect(self.btnSprawdz_clicked)       # Przypisujemy przycisk do procedury obłsugi zdarzenia
        self.actionZakoncz.triggered.connect(self.menuZakoncz_wybrane)  # Przisujemy pozyjce w menu Zakoncz od procedury obsługi zdarzenia
        self.lblKomunikat.setText("")
        self.lblStatus.setText(u"Pozostało ci " + str(proby) + u" prób.")

    def btnSprawdz_clicked(self, event):
        global koniec, propozycja, proby
        propozycja = self.spinBox1.value()       # Pobranie propozycji gracza
        if propozycja != sekret and proby > 1:
            if propozycja < sekret:
                self.lblKomunikat.setText(u"Za mała, psubracie!")
            elif propozycja > sekret:
                self.lblKomunikat.setText(u"Za duża, szczurze lądowy!")
            proby = proby - 1                         # Zwiększenie liczby prób
            self.lblStatus.setText(u"Pozostało ci " + str(proby) + u" prób.")
                
        elif propozycja == sekret:   # Gracz odgadł liczbę
            self.lblKomunikat.setText(u"Stop! Udało Ci się! Odgadłeś moją tajemną liczbę!")
            self.lblStatus.setText("")
        else:                  # Graczowi skończyły się próby
            self.lblKomunikat.setText(u"Wykorzystałeś wszystkie próby! Powodzenia następnym razem, koleżko!")
            self.lblStatus.setText("Tajemna liczba to "+ str(sekret))
            
    def menuZakoncz_wybrane(self):              # procedura obsługi zdarzenia maenu Plik/Zakoncz
        self.close()                           # 

aplikacja = QtGui.QApplication(sys.argv)
mojeOkno = MojaKlasaOkna(None)
mojeOkno.show()
aplikacja.exec_() 
    
