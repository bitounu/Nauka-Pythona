# Listing_11-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# program wyznaczaj�cy wszystkie mo�liwe kombinacje dodatk�w do hot doga

print "\tPar�wka\tBu�ka\tKetchup\tMusztar\tCebula"
licznik = 1
for parowka in [0, 1]:                                                  # p�tla parowka
    for bulka in [0, 1]:                                                # p�tla bulka
        for ketchup in [0, 1]:                                          # p�tla ketchup
            for musztarda in [0, 1]:                                    # p�tla musztarda
                for cebula in [0, 1]:                                   # p�tla cebula
                    print "#", licznik, "\t",
                    print parowka, "\t", bulka, "\t", ketchup, "\t",
                    print musztarda, "\t", cebula
                    licznik = licznik + 1

        
