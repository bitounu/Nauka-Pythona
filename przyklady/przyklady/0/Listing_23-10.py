# -*- coding: utf-8 -*-
# Listing_23-10.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone Ăłsemki - tura komputera

# ZwrĂłÄ‡ uwagÄ™, ĹĽe to nie jest kompletny program.  Aby utowrzyÄ‡ kompletny program gry w Szalone Ăłsemki,
#   naleĹĽy poĹ‚Ä…czyÄ‡ poniĹĽszy kod z posostaĹ‚ymi elemenatmi.

def tura_komputera():
    global reka_komputera, talia, karta_wiodaca, kolor_wiodacy, zablokowani
    do_wyboru = []
    for karta in reka_komputera:
        if karta.figura == '8':         # Komputer zagrywa 8
            reka_komputera.remove(karta)    
            karta_wiodaca = karta
            print u" Komputer zagraĹ‚ ", karta.krotka_nazwa
            #sumy kolorĂłw: [dzwonki, serce, wino, ĹĽoĹ‚Ä™dzie]
            sumy_kolorow = [0, 0, 0, 0]     # Zliczamy karty kaĹĽdego koloru
            for kolor in range(1, 5):
                for karta in reka_gracza:
                    if karta.kolor_id == kolor:
                        sumy_kolorow[kolor-1] += 1
            kolor_najwiecej = 0         # Kolor ktĂłrego komputer ma na rÄ™ce najwiÄ™cej, staje siÄ™ kolorem wiodÄ…cym
            for i in range (4):
                if sumy_kolorow[i] > kolor_najwiecej:
                    kolor_najwiecej = i
                    
            # ustawiamy kolor wiodÄ…cy        
            if kolor_najwiecej == 0: kolor_wiodacy = "Dzwonki"
            if kolor_najwiecej == 1: kolor_wiodacy = "Serce"
            if kolor_najwiecej == 2: kolor_wiodacy = "Wino"
            if kolor_najwiecej == 3: kolor_wiodacy = u"ZoĹ‚Ä™dzie"
            print u"Komputer zmieniĹ‚ kolor na ", kolor_wiodacy
            return      # Koniec tury komputera â€” powrĂłt do gĹ‚Ăłwnej pÄ™tli 
        else:
            if karta.kolor == kolor_wiodacy:    # Sprawdzamy, ktĂłre karty moĹĽna zagraÄ‡
                do_wyboru.append(karta)
            elif karta.figura == karta_wiodaca.figura:
                do_wyboru.append(karta)

    if len(do_wyboru) > 0:
        najlepiej_zagrac = do_wyboru[0]             # Sprawdzmy, ktĂłra z kart bÄ™dzie najlepszym wyborem
        for karta in do_wyboru:
            if karta.wartosc > najlepiej_zagrac.wartosc:
                najlepiej_zagrac = karta
        reka_komputera.remove(najlepiej_zagrac)     # Komputer zagrywa kartÄ™
        karta_wiodaca = najlepiej_zagrac
        kolor_wiodacy = karta_wiodaca.kolor
        print u"Komputer zagraĹ‚ ", najlepiej_zagrac.krotka_nazwa

    else:                                           # Nie moĹĽna zagraÄ‡ ĹĽadnej karty, wiÄ™c dobieramy kartÄ™ ze stosu,
        if len(talia) >0:                           # jeĹĽeli leĹĽÄ… na nim jeszcze jakies karty
            nastepna_karta = random.choice(talia)
            reka_komputera.append(nastepna_karta)
            talia.remove(nastepna_karta)
            print u"Komputer dobraĹ‚ kartÄ™"
        else:                                       # Na stosie nie ma juz kart, komputer jest zablokowany
            print "Komputer jest zablokowany"
            zablokowani += 1
    print u"Komputerowi pozostaĹ‚y %i karty" % (len(reka_komputera))

