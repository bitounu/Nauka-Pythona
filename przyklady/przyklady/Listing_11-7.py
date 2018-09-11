# Listing_11-7.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# program wyznaczaj¹cy wszystkie mo¿liwe kombinacje dodatków do hot doga
# dodatkowo wyliczana jest suma kalorii dodatków

# Lista zawieraj¹ca liczbê kalorii ka¿dego sk³adnika
par_kal = 140
bulka_kal = 120
muszt_kal = 20
ket_kal = 80
ceb_kal = 40

print "\tParówka\tBu³ka\tKetchup\tMusztar\tCebula\tKalorie"  # Wyœwietlamy nag³ówki kolumn

# Pêtle zagnie¿d¿one
licznik = 1
for parowka in [0, 1]:               # parowka jest pêtl¹ zewnêtrzn¹
    for bulka in [0, 1]:
        for ketchup in [0, 1]:
            for musztarda in [0, 1]:
                for cebula in [0, 1]:
                    # Kalorie obliczamy w pêtli wewnêtrznej
                    # zwróæ uwagê na symbol kontynuacji linii
                    razem_kal = (parowka * par_kal) + (bulka * bulka_kal) + \
                        (musztarda * muszt_kal) + (ketchup * ket_kal) + \
                        (cebula * ceb_kal)
                    print "#", licznik, "\t",
                    print parowka, "\t", bulka, "\t", ketchup, "\t",
                    print musztarda, "\t", cebula,
                    print "\t", razem_kal
                    licznik = licznik + 1


                                    
