# Listing_11-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# program wyznaczaj¹cy wszystkie mo¿liwe kombinacje dodatków do hot doga

print "\tParówka\tBu³ka\tKetchup\tMusztar\tCebula"
licznik = 1
for parowka in [0, 1]:                                                  # pêtla parowka
    for bulka in [0, 1]:                                                # pêtla bulka
        for ketchup in [0, 1]:                                          # pêtla ketchup
            for musztarda in [0, 1]:                                    # pêtla musztarda
                for cebula in [0, 1]:                                   # pêtla cebula
                    print "#", licznik, "\t",
                    print parowka, "\t", bulka, "\t", ketchup, "\t",
                    print musztarda, "\t", cebula
                    licznik = licznik + 1

        
