# Listing_7-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wykorzystanie operatorów porównania

liczba1 = float(raw_input("Wprowadź pierwszą liczbę: "))
liczba2 = float(raw_input("Wprowadź drugą liczbę: "))
if liczba1 < liczba2:
    print liczba1, "jest mniejsze niż", liczba2
if liczba1 > liczba2:
    print liczba1, "jest większe niż", liczba2
if liczba1 == liczba2:  # Zwróć uwagę na to, że to podwójny symbol równości
    print liczba1, "jest równe", liczba2
if liczba1 != liczba2:
    print liczba1, "nie jest równe", liczba2

