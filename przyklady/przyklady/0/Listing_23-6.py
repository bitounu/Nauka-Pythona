# Listing_23-6.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Główna pętla programu Szalone ósemki

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

inicjalizacja_kart()
while not koniec_partii:
    zablokowani = 0
    tura_gracza()
    if len(reka_gracza) == 0:       # Na ręce gracza nie ma już żadnych kart, więc wygrywa on partię
        koniec_partii = True
        print
        print u"Wygrałeś!"
    if not koniec_partii:
        tura_komputera()
    if len(reka_komputera) == 0:    # Na ręce komputera nie ma już żadnych kart, więc wygrywa on partię
        koniec_partii = True
        print
        print u"Wygrał komputer!"
    if zablokowani >= 2:        # Gracze są zablokowani, więc kończymy partię
        koniec_partii = True
        print u"Gracze są zablokowani. KONIEC GRY."
