# Listing_22-6.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Zapisywanie listy za pomoc¹ modu³u pickle

import pickle
moja_lista = ['Marek', 73, 'Witaj', 81.9876e-13]
plik_marynowanie = open('zamarynowana_lista.mar', 'w')
pickle.dump(moja_lista, plik_marynowanie)
plik_marynowanie.close()
