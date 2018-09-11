# Listing_13-3
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Funkcja z dwoma argumentami

def wyswietlMojAdres(imieNazwisko, numerDomu):
    print imieNazwisko
    print "ul. Kasztanowa",     # przecinek sprawia, że ulica i numer domu wyświetlą się w jednej linii
    print numerDomu
    print "44-100 Gliwice"
    print "Polska"
    print

wyswietlMojAdres("Maciek Kowalski", "45")   # przekazujemy do funkcji 2 argumenty
wyswietlMojAdres("Jerzy Grabowski", "64")
wyswietlMojAdres("Tomasz Rawicz", "22")
wyswietlMojAdres("Tadeusz Styczeń", "36")

