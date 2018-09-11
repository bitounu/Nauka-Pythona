# Listing_24-4.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Program wirtualnego zwierzaka

import sys, pickle,datetime
from PyQt4 import QtCore, QtGui, uic

klasa_formularza, klasa_bazowa = uic.loadUiType("wirtualnyZwierzak.ui")

class MojFormularz(klasa_bazowa, klasa_formularza):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # Inicjalizujemy warto�ci
        self.doktor = False
        self.wyprowadzanie = False
        self.sen = False
        self.zabawa = False
        self.jedzenie = False
        self.time_cycle = 0
        self.glod = 0
        self.szczescie = 8
        self.zdrowie = 8
        self.wymusObudzenie = False
        # Listy zawieraj�ce rysunki animacji
        self.senRysunki = ["sleep1.gif","sleep2.gif","sleep3.gif",
        "sleep4.gif"]
        self.jedzenieRysunki = ["eat1.gif", "eat2.gif"]
        self.wyprowadzanieRysunki = ["walk1.gif", "walk2.gif", "walk3.gif",
        "walk4.gif"]
        self.zabawaRysunki = ["play1.gif", "play2.gif"]
        self.doktorRysunki = ["doc1.gif", "doc2.gif"]
        self.normalneRysunki = ["pet1.gif", "pet2.gif", "pet3.gif"]
        self.listaRysunkow = self.normalneRysunki
        self.rysunekIndeks = 0

        # ��czymy przyciski na pasku narz�dzi z procedurami obs�ugi zdarzenia
        self.actionStop.triggered.connect(self.stop_klikniety)
        self.actionNakarm.triggered.connect(self.nakarm_klikniety)
        self.actionWyprowadz.triggered.connect(self.wyprowadz_klikniety)
        self.actionZabawa.triggered.connect(self.zabawa_klikniety)
        self.actionDoktor.triggered.connect(self.doktor_klikniety)

        # Ustawiamy timery
        self.mojTimer1 = QtCore.QTimer(self)
        self.mojTimer1.start(500)
        self.mojTimer1.timeout.connect(self.animacja_timer)
        
        self.mojTimer2 = QtCore.QTimer(self)
        self.mojTimer2.start(5000)
        self.mojTimer2.timeout.connect(self.tykniecie_timer)
        
        plikUchwyt = True
        try:    # Pr�bujemy otworzy� plik
            plik = open("zapisane_dane_wz.pkl", "r")
        except:
            plikUchwyt = False
        if plikUchwyt:
            zapis_lista = pickle.load(plik) # Odczytujemy dane z pliku
            plik.close()
        else:       # Je�eli pliku nie ma, ustawiamy domy�lne warto�ci
            zapis_lista = [8, 8, 0, datetime.datetime.now(), 0]
            
        self.szczescie = zapis_lista[0]
        self.zdrowie = zapis_lista[1]
        self.glod = zapis_lista[2]
        znacznik_czasu_wtedy = zapis_lista[3]
        self.cykl_zegara = zapis_lista[4]

        # Sprawdzamy, ile czasu up�yn�o od ostatniego uruchomienia programu
        roznica = datetime.datetime.now() - znacznik_czasu_wtedy
        tykniecia = roznica.seconds / 50

        # Symulujemy wszystkie tykni�cia, kt�re nast�pi�y od momentu ostatniego uruchomienia programu
        for i in range(0, tykniecia):
            self.cykl_zegara += 1
            if self.cykl_zegara == 60:
                self.cykl_zegara = 0
            if self.cykl_zegara <= 48:  # Obudzony
                self.sen = False
                if self.glod < 8:
                    self.glod += 1

            else:       # �pi
                self.sen = True
                if self.glod < 8 and self.cykl_zegara % 3 == 0:
                    self.glod += 1
            if self.glod == 7 and (self.cykl_zegara % 2 ==0) \
                              and self.zdrowie > 0:
                self.zdrowie -= 1
            if self.glod == 8 and self.zdrowie > 0:
                self.zdrowie -=1

        # Dobieramy odpowiedni� animacj�        
        if self.sen:
            self.listaRysunkow = self.senRysunki
        else:
            self.listaRysunkow = self.normalneRysunki

    # Zanim wykonamy akcj�, sprawdzamy, czy zwierzak �pi
    def sprawdz_pobudka(self):
        if self.sen:
            wynik = (QtGui.QMessageBox.warning(self, 'UWAGA',
u"Czy na pewno chcesz obudzi� zwierzaka? B�dzie bardzo niezadowolony!",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
            QtGui.QMessageBox.No))
            if wynik == QtGui.QMessageBox.Yes:
                self.sen = False
                self.szczescie -= 4
                self.wymusObudzenie = True
                return True
            else:
                return False
        else:
            return True

    # Procedura obs�ugi zdarzenia przycisku Doktor
    def doktor_klikniety(self):
        if self.sprawdz_pobudka():
            self.listaRysunkow = self.doktorRysunki
            self.doktor = True
            self.wyprowadzanie = False
            self.jedzenie = False
            self.zabawa = False

    # Procedura obs�ugi zdarzenia przycisku Nakarm
    def nakarm_klikniety(self):
        if self.sprawdz_pobudka():
            self.listaRysunkow = self.jedzenieRysunki
            self.jedzenie = True
            self.wyprowadzanie = False
            self.zabawa = False
            self.doktor = False

    # Procedura obs�ugi zdarzenia przycisku Zabawa
    def zabawa_klikniety(self):
        if self.sprawdz_pobudka():
            self.listaRysunkow = self.zabawaRysunki
            self.zabawa = True
            self.wyprowadzanie = False
            self.jedzenie = False
            self.doktor = False

    # Procedura obs�ugi zdarzenia przycisku Spacer
    def wyprowadz_klikniety(self):
        if self.sprawdz_pobudka():
            self.listaRysunkow = self.wyprowadzanieRysunki
            self.wyprowadzanie = True
            self.jedzenie = False
            self.zabawa = False
            self.doktor = False

    # Procedura obs�ugi zdarzenia przycisku Stop
    def stop_klikniety(self):
        if not self.sen:
            self.listaRysunkow = self.normalneRysunki
            self.wyprowadzanie = False
            self.jedzenie = False
            self.zabawa = False
            self.doktor = False

    # Procedura obs�ugi zdarzenia timera animacji
    def animacja_timer(self):
        if self.sen and not self.wymusObudzenie:
            self.listaRysunkow = self.senRysunki
        self.rysunekIndeks += 1
        if self.rysunekIndeks >= len(self.listaRysunkow):
            self.rysunekIndeks = 0
        ikona = QtGui.QIcon()

        # Aktualizujemy rysunek zwierzaka
        biezacy_rysunek = self.listaRysunkow[self.rysunekIndeks]
        ikona.addPixmap(QtGui.QPixmap(biezacy_rysunek),
                QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.zwierzakPic.setIcon(ikona)
        self.pasekPostepu_1.setProperty("value", (8-self.glod)*(100/8.0))
        self.pasekPostepu_2.setProperty("value", self.szczescie*(100/8.0))
        self.pasekPostepu_3.setProperty("value", self.zdrowie*(100/8.0))

    # Pocz�tek procedury obs�ugi zdarzenia g��wnego timera
    def tykniecie_timer(self):
        self.cykl_zegara += 1

        # Sprawdzamy, czy zwierzak �pi
        if self.cykl_zegara == 60:
            self.cykl_zegara = 0
        if self.cykl_zegara <= 48 or self.wymusObudzenie:
            self.sen = False
        else:
            self.sen = True
        if self.cykl_zegara == 0:
            self.wymusObudzenie = False

        # W zale�no�ci od aktywno�ci dodajemy lub odejmujemy warto��    
        if self.doktor:
            self.zdrowie += 1
            self.glod += 1
        elif self.wyprowadzanie and (self.cykl_zegara % 2 == 0):
            self.szczescie += 1
            self.zdrowie += 1
            self.glod += 1
        elif self.zabawa:
            self.szczescie += 1
            self.glod += 1
        elif self.jedzenie:
            self.glod -= 2
        elif self.sen:
            if self.cykl_zegara % 3 == 0:
                self.glod += 1
        else:
            self.glod += 1
            if self.cykl_zegara % 2 == 0:
                self.szczescie -= 1

        # Sprawdzamy, czy warto�� znajduje si� w okre�lonym przedziale        
        if self.glod > 8: self.glod = 8
        if self.glod < 0: self.glod = 0
        if self.glod == 7 and (self.cykl_zegara % 2 ==0) :
            self.zdrowie -= 1
        if self.glod == 8:
            self.zdrowie -=1
        if self.zdrowie > 8: self.zdrowie = 8
        if self.zdrowie < 0: self.zdrowie = 0
        if self.szczescie > 8: self.szczescie = 8
        if self.szczescie < 0: self.szczescie = 0

        # Aktualizujemy paski post�pu
        self.pasekPostepu_1.setProperty("value", (8-self.glod)*(100/8.0))
        self.pasekPostepu_2.setProperty("value", self.szczescie*(100/8.0))
        self.pasekPostepu_3.setProperty("value", self.zdrowie*(100/8.0))

    def closeEvent(self, zdarzenie):
        plik = open("zapisane_dane_wz.pkl", "w")
        zapis_lista= [self.szczescie, self.zdrowie, self.glod, \
                    datetime.datetime.now(), self.time_cycle]
        pickle.dump(zapis_lista, plik)
        zdarzenie.accept() 

aplikacja = QtGui.QApplication(sys.argv)
mojaAplikacja = MojFormularz()
mojaAplikacja.show()
aplikacja.exec_()

