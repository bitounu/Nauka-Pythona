# TIO_CH12_5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 5, z rozdzia�u 12.

slownik_uzytkownika = {}
while 1:
    polecenie = raw_input("'d' - aby doda� has�o, 'w' - aby wyszuka� has�o, 'x' - aby wyj��")

    if polecenie == "d":
        haslo = raw_input("Wprowad� has�o: ")
        definicja = raw_input("Wprowad� definicj�: ")
        slownik_uzytkownika[haslo] = definicja
        print "Has�o dodane!"

    elif polecenie == "w":
        haslo = raw_input("Wprowad� has�o: ")
        if haslo in slownik_uzytkownika.keys():
            print slownik_uzytkownika[haslo]
        else:
            print "Tego has�a nie ma jeszcze w s�owniku."
            
    elif polecenie == 'x':
        break


