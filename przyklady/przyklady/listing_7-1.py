# Listing_7-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wykorzystanie operator�w por�wnania

liczba1 = float(raw_input("Wprowad� pierwsz� liczb�: "))
liczba2 = float(raw_input("Wprowad� drug� liczb�: "))
if liczba1 < liczba2:
    print liczba1, "jest mniejsze ni�", liczba2
if liczba1 > liczba2:
    print liczba1, "jest wi�ksze ni�", liczba2
if liczba1 == liczba2:  # Zwr�� uwag� na to, �e to podw�jny symbol r�wno�ci
    print liczba1, "jest r�wne", liczba2
if liczba1 != liczba2:
    print liczba1, "nie jest r�wne", liczba2

