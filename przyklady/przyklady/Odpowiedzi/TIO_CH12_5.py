# TIO_CH12_5.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 5, z rozdzia³u 12.

slownik_uzytkownika = {}
while 1:
    polecenie = raw_input("'d' - aby dodaæ has³o, 'w' - aby wyszukaæ has³o, 'x' - aby wyjœæ")

    if polecenie == "d":
        haslo = raw_input("WprowadŸ has³o: ")
        definicja = raw_input("WprowadŸ definicjê: ")
        slownik_uzytkownika[haslo] = definicja
        print "Has³o dodane!"

    elif polecenie == "w":
        haslo = raw_input("WprowadŸ has³o: ")
        if haslo in slownik_uzytkownika.keys():
            print slownik_uzytkownika[haslo]
        else:
            print "Tego has³a nie ma jeszcze w s³owniku."
            
    elif polecenie == 'x':
        break


