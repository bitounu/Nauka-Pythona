# Listing_15-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z modu�u

# w module moj_modul znajduje si� definicja funkcji c_na_f()
import moj_modul

celsjusze = float(raw_input("Wprowad� temperatur� w stopniach Celsjusza: "))
fahrenheity = c_na_f(celsjusze)
print "To ", fahrenheity, " stopni Fahrenheita"


# Po uruchomieniu tego kodu pojawi s� komunikat b��du
# Wyja�ni� to w dalszej cz�ci rozdzia�u 15.
