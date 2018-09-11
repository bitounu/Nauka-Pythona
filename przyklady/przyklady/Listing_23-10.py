# -*- coding: utf-8 -*-
# Listing_23-10.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Szalone ósemki - tura komputera

# Zwróć uwagę, że to nie jest kompletny program.  Aby utowrzyć kompletny program gry w Szalone ósemki,
#   należy połączyć poniższy kod z posostałymi elemenatmi.

def tura_komputera():
    global reka_komputera, talia, karta_wiodaca, kolor_wiodacy, zablokowani
    do_wyboru = []
    for karta in reka_komputera:
        if karta.figura == '8':         # Komputer zagrywa 8
            reka_komputera.remove(karta)    
            karta_wiodaca = karta
            print u" Komputer zagrał ", karta.krotka_nazwa
            #sumy kolorów: [dzwonki, serce, wino, żołędzie]
            sumy_kolorow = [0, 0, 0, 0]     # Zliczamy karty każdego koloru
            for kolor in range(1, 5):
                for karta in reka_gracza:
                    if karta.kolor_id == kolor:
                        sumy_kolorow[kolor-1] += 1
            kolor_najwiecej = 0         # Kolor którego komputer ma na ręce najwięcej, staje się kolorem wiodącym
            for i in range (4):
                if sumy_kolorow[i] > kolor_najwiecej:
                    kolor_najwiecej = i
                    
            # ustawiamy kolor wiodący        
            if kolor_najwiecej == 0: kolor_wiodacy = "Dzwonki"
            if kolor_najwiecej == 1: kolor_wiodacy = "Serce"
            if kolor_najwiecej == 2: kolor_wiodacy = "Wino"
            if kolor_najwiecej == 3: kolor_wiodacy = u"Zołędzie"
            print u"Komputer zmienił kolor na ", kolor_wiodacy
            return      # Koniec tury komputera — powrót do głównej pętli 
        else:
            if karta.kolor == kolor_wiodacy:    # Sprawdzamy, które karty można zagrać
                do_wyboru.append(karta)
            elif karta.figura == karta_wiodaca.figura:
                do_wyboru.append(karta)

    if len(do_wyboru) > 0:
        najlepiej_zagrac = do_wyboru[0]             # Sprawdzmy, która z kart będzie najlepszym wyborem
        for karta in do_wyboru:
            if karta.wartosc > najlepiej_zagrac.wartosc:
                najlepiej_zagrac = karta
        reka_komputera.remove(najlepiej_zagrac)     # Komputer zagrywa kartę
        karta_wiodaca = najlepiej_zagrac
        kolor_wiodacy = karta_wiodaca.kolor
        print u"Komputer zagrał ", najlepiej_zagrac.krotka_nazwa

    else:                                           # Nie można zagrać żadnej karty, więc dobieramy kartę ze stosu,
        if len(talia) >0:                           # jeżeli leżą na nim jeszcze jakies karty
            nastepna_karta = random.choice(talia)
            reka_komputera.append(nastepna_karta)
            talia.remove(nastepna_karta)
            print u"Komputer dobrał kartę"
        else:                                       # Na stosie nie ma juz kart, komputer jest zablokowany
            print "Komputer jest zablokowany"
            zablokowani += 1
    print u"Komputerowi pozostały %i karty" % (len(reka_komputera))

