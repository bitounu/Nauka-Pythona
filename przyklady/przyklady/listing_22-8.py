# Listing_22-8.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Gra Wysielec, wykorzystuj�ca PyQt

import sys
from PyQt4 import QtCore, QtGui, uic
import random

klasa_formularza = uic.loadUiType("wisielec.ui")[0]

# odszukujemy po�o�enie(a) liter w s�owie
def znajdz_litery(litera, lancuch):
    polozenia = []
    poczatek = 0
    while lancuch.find(litera, poczatek, len(lancuch)) != -1:
        polozenie = lancuch.find(litera, poczatek, len(lancuch))
        polozenia.append(polozenie)
        poczatek = polozenie + 1
    return polozenia

# je�li gracz odgad� liter�, zast�pujemy ni� znaki my�linka
def zamien_litery(lancuch, polozenia, litera):
    nowy_lancuch = ''
    for i in range (0, len(lancuch)):
        if i in polozenia:
            nowy_lancuch = nowy_lancuch + litera
        else:
            nowy_lancuch = nowy_lancuch + lancuch[i]
    return nowy_lancuch

# na pocz�tku programu zamieniamy wszystkie litery w s�owie na znaki my�lnika
def myslniki(slowo):
    litery = "abcdefghijklmnopqrstuvwxyz"
    nowy_lancuch = ''
    for i in slowo:
        if i in litery:
            nowy_lancuch += "-"
        else:
            nowy_lancuch += i
    return nowy_lancuch

class MojWidzet(QtGui.QMainWindow, klasa_formularza):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_sprawdz.clicked.connect(self.btn_sprawdz_klikniety)        # ��czymy zdarzenia z procedurami obs�ugi zdarze�
        self.actionZako_cz.triggered.connect(self.menuZakoncz_wybrane)      #
        self.fragmenty_ciala = [self.glowa, self.tulow, self.lewaReka, self.lewaNoga,   # Cz�ci cia�a wisielca
        self.prawaReka, self.prawaNoga]                                                 #        
        self.szubienica = [self.linia1, self.linia2, self.linia3, self.linia4]      # cz�c i szubienicy
        self.widoczne_fragmenty = 0
        self.biezaceSlowo = ""

        # �adujemy list� s��w
        plik=open("slowa.txt", 'r')
        self.linie = plik.readlines()
        plik.close()
        self.nowa_gra()

    def nowa_gra(self):
        self.odpowiedzi.setText("")
        self.biezaceSlowo = random.choice(self.linie)           # wybieramy losowo jedno s�owo z listy
        self.biezaceSlowo = self.biezaceSlowo.strip()
        for i in self.fragmenty_ciala:                          # ukrywamy wisielca
            i.setFrameShadow(QtGui.QFrame.Plain)                #
            i.setHidden(True)                                   #
        for i in self.szubienica:
            i.setFrameShadow(QtGui.QFrame.Plain)
        self.slowo.setText(myslniki(self.biezaceSlowo))         # wywo�ujemy funkcj� kt�ra zast�puje wszystkie litery znakami my�lnika
        self.fragmenty_widoczne = 0

    # gracz wprowadza liter� lub s�owo
    def btn_sprawdz_klikniety(self):
        odpowiedz = str(self.odpowiedzText.text())
        if str(self.odpowiedzi.text()) != "":
            self.odpowiedzi.setText(str(self.odpowiedzi.text())+", "+odpowiedz)
        else:
            self.odpowiedzi.setText(odpowiedz)
        if len(odpowiedz) == 1:                                             # gracz wprowadzi� liter�
            if odpowiedz in self.biezaceSlowo:                              #
                polozenia = znajdz_litery(odpowiedz, self.biezaceSlowo)     #
                self.slowo.setText(zamien_litery(str(self.slowo.text()),    #
                                               polozenia,odpowiedz))        #
                if str(self.slowo.text()) == self.biezaceSlowo:             #
                    self.wygrana()                                          #
            else:
                self.zle()
        else:                                                           # gracz wprowadzi� s�owo
            if odpowiedz == self.biezaceSlowo:                          #
                self.wygrana()                                          #
            else:                                                       #
                self.zle()                                              #
        self.odpowiedzText.setText("")

    def wygrana(self):                                                  # wy�wietlamy okno dialogowe informuj�ce o wygranej
        QtGui.QMessageBox.information(self,"Wisielec","Wygra�e�!")      #
        self.nowa_gra()                                                 #

    # obs�uga z�ej odpowiedzi
    def zle(self):
        self.fragmenty_widoczne += 1
        for i in range(self.fragmenty_widoczne):                        # ods�aniamy kolejn� cz�� cia�a wisielca
            self.fragmenty_ciala[i].setHidden(False)                    #
        if self.fragmenty_widoczne == len(self.fragmenty_ciala):
            komunikat = "Przegra�e�. S�owo to: " + self.biezaceSlowo    # gracz przegrywa
            QtGui.QMessageBox.warning(self,"Wisielec", komunikat)       #
            self.nowa_gra()

    def menuZakoncz_wybrane(self):
        self.close()
aplikacja = QtGui.QApplication(sys.argv)
moja_aplikacja = MojWidzet(None)
moja_aplikacja.show()
aplikacja.exec_()

