# Listing_15-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z modułu

# w module moj_modul znajduje się definicja funkcji c_na_f()
import moj_modul

celsjusze = float(raw_input("Wprowadź temperaturę w stopniach Celsjusza: "))
fahrenheity = c_na_f(celsjusze)
print "To ", fahrenheity, " stopni Fahrenheita"


# Po uruchomieniu tego kodu pojawi sę komunikat błędu
# Wyjaśnię to w dalszej części rozdziału 15.
