# Listing_15-2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Korzystanie z modu³u

# w module moj_modul znajduje siê definicja funkcji c_na_f()
import moj_modul

celsjusze = float(raw_input("WprowadŸ temperaturê w stopniach Celsjusza: "))
fahrenheity = c_na_f(celsjusze)
print "To ", fahrenheity, " stopni Fahrenheita"


# Po uruchomieniu tego kodu pojawi sê komunikat b³êdu
# Wyjaœniê to w dalszej czêœci rozdzia³u 15.
