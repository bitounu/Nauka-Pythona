# Listing_5-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Pobieranie danych z pliku umieszczonego w sieci

import urllib2
plik = urllib2.urlopen('http://helloworldbook2.com/data/message.txt')
wiadomosc = plik.read()
print wiadomosc

