# Listing_7-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Wykorzystanie operatorów porównania

liczba1 = float(raw_input("WprowadŸ pierwsz¹ liczbê: "))
liczba2 = float(raw_input("WprowadŸ drug¹ liczbê: "))
if liczba1 < liczba2:
    print liczba1, "jest mniejsze ni¿", liczba2
if liczba1 > liczba2:
    print liczba1, "jest wiêksze ni¿", liczba2
if liczba1 == liczba2:  # Zwróæ uwagê na to, ¿e to podwójny symbol równoœci
    print liczba1, "jest równe", liczba2
if liczba1 != liczba2:
    print liczba1, "nie jest równe", liczba2

