# Listing_24-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Zapisywanie czasu do pliku za pomocą modułu pickle

import datetime, pickle
import os

pierwszy_raz = True
if os.path.isfile("ostatnie_uruchomienie.pkl"):     # sprawdzamy, czy na dysku znajduje się plik
    plik = open("ostatnie_uruchomienie.pkl", 'r')   # otwieramy plik w trybie do odczytu 
    ostatnie_uruchomienie = pickle.load(plik)       # odczytujemy obiekt typu datetime
    plik.close()
    print u"Ostatni raz uruchomiłeś program ", ostatnie_uruchomienie
    pierwszy_raz = False

plik = open("ostatnie_uruchomienie.pkl", 'w')       # otwieramy (lub tworzymy) plik w trybie do zapisu
pickle.dump(datetime.datetime.now(), plik)          # zapisujemy obiekt typu datetime zawierający bieżący czas
plik.close()
if pierwszy_raz:
    print "Utworzono nowy plik."
