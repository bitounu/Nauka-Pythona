# Listing_5-3.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Konwersja temperatury z wykorzystaniem funkcji raw_input()

print "Program konwertuj�cy temperatur� ze stopni Fahrenheita na stopnie Celsjusza"
print "Wprowad� temperatur� w stopniach Fahrenheita: ",
fahrenheity = float(raw_input()) # Pobieramy od u�ytkownika liczb� stopni Fahrenheita
celsjusze = (fahrenheity - 32) * 5.0 / 9
print "To",                      # Zwr�� uwag� na przecinki
print celsjusze,                 # w tych liniach
print "stopni Celsjusza"

