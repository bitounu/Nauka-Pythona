# Listing_22-7.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odmarynowanie za pomoc¹ funkcji load()

import pickle
plik_marynowanie = open('zamarynowana_lista.mar', 'r')
przywrocona_lista = pickle.load(plik_marynowanie)
plik_marynowanie.close()

print przywrocona_lista

