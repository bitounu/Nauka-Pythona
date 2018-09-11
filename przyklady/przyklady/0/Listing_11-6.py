# Listing_11-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# program wyznaczający wszystkie możliwe kombinacje dodatków do hot doga

print "\tParówka\tBułka\tKetchup\tMusztar\tCebula"
licznik = 1
for parowka in [0, 1]:                                                  # pętla parowka
    for bulka in [0, 1]:                                                # pętla bulka
        for ketchup in [0, 1]:                                          # pętla ketchup
            for musztarda in [0, 1]:                                    # pętla musztarda
                for cebula in [0, 1]:                                   # pętla cebula
                    print "#", licznik, "\t",
                    print parowka, "\t", bulka, "\t", ketchup, "\t",
                    print musztarda, "\t", cebula
                    licznik = licznik + 1

        
