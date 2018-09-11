# -*- coding: utf-8 -*-
# Crazy_eights.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Final Crazy Eights card game (text-based)

import random
from karty import Karta

def inicjalizacja_kart():
    global talia, reka_gracza, reka_komputera, karta_wiodaca, kolor_wiodacy
    talia = []
    for kolor in range(1, 5):
        for figura in range(1, 14):
            nowa_karta = Karta(kolor, figura)
            if figura == 8:
                nowa_karta.wartosc = 50
            talia.append(nowa_karta)

    reka_gracza = []
    for karty in range(0, 5):
        karta = random.choice(talia)
        reka_gracza.append(karta)
        talia.remove(karta)
    
    reka_komputera = []    
    for karty in range(0, 5):
        karta = random.choice(talia)
        reka_komputera.append(karta)
        talia.remove(karta)
        
    karta = random.choice(talia)
    talia.remove(karta)
    karta_wiodaca  = karta
    kolor_wiodacy = karta_wiodaca.kolor

def pobierz_nowy_kolor():
    global kolor_wiodacy
    kolor_wybrany = False
    while not kolor_wybrany:
        kolor = raw_input("Wybierz kolor: ")
        if kolor.lower() == 'd':
            kolor_wiodacy = "Dzwonki"
            kolor_wybrany = True
        elif kolor.lower() == 'w':
            kolor_wiodacy = "Wino"
            kolor_wybrany = True
        elif kolor.lower() == 's':
            kolor_wiodacy = "Serce"
            kolor_wybrany = True
        elif kolor.lower() == 'z':
            kolor_wiodacy = u"ZoĹ‚Ä™dzie"
            kolor_wybrany = True
        else:
            print u"NieprawidĹ‚owy kolor. SprĂłbuj ponownie. ",
    print u"WybraĹ‚eĹ›", kolor_wiodacy

def tura_gracza():
    global talia, reka_gracza, zablokowani, karta_wiodaca, kolor_wiodacy
    dobre_zagranie = False
    czy_osemka = False
    print u"\nTwoja rÄ™ka: ",
    for karta in reka_gracza:
        print karta.krotka_nazwa,
    print u" Karta wiodÄ…ca: ", karta_wiodaca.krotka_nazwa
    if karta_wiodaca.figura == '8':
        print u" Kolor wiodÄ…cy", kolor_wiodacy
    print u"Co chcesz zrobiÄ‡? ",
    odpowiedz = raw_input (u"WprowadĹş nazwÄ™ karty lub wpisz 'Dobierz', aby dobraÄ‡ kartÄ™: " )
    dobre_zagranie = False
    while not dobre_zagranie:
        wybrana_karta = None
        while wybrana_karta == None:
            if odpowiedz.lower() == 'dobierz':
                dobre_zagranie = True
                if len(talia) > 0:
                    karta = random.choice(talia)
                    reka_gracza.append(karta)
                    talia.remove(karta)
                    print u"DobraĹ‚eĹ›", karta.krotka_nazwa
                else:
                    print u"Na stosie nie ma juĹĽ kart"
                    zablokowani += 1
                return
            else:
                for karta in reka_gracza:
                    if odpowiedz.upper() == karta.krotka_nazwa:
                        wybrana_karta = karta
                if wybrana_karta == None:
                    odpowiedz = raw_input(u"Nie masz na rÄ™ce tej karty. SprĂłbuj ponownie:")

        if wybrana_karta.figura == '8':
            dobre_zagranie = True
            czy_osemka = True
        elif wybrana_karta.kolor == kolor_wiodacy:
            dobre_zagranie = True
        elif wybrana_karta.figura == karta_wiodaca.figura:
            dobre_zagranie = True

        if not dobre_zagranie:
            odpowiedz = raw_input(u"NieprawidĹ‚owe zagranie. SprĂłbuj ponownie: ")

            
    reka_gracza.remove(wybrana_karta)
    karta_wiodaca  = wybrana_karta
    kolor_wiodacy = karta_wiodaca.kolor
    print u"ZagraĹ‚eĹ›", wybrana_karta.krotka_nazwa
    if czy_osemka:
        pobierz_nowy_kolor()
        
 

def tura_komputera():
    global reka_komputera, talia, karta_wiodaca, kolor_wiodacy, zablokowani
    do_wyboru = []
    for karta in reka_komputera:
        if karta.figura == '8':
            reka_komputera.remove(karta)
            karta_wiodaca = karta
            print u" Komputer zagraĹ‚ ", karta.krotka_nazwa
            #sumy kolorĂłw: [dzwonki, serce, wino, ĹĽoĹ‚Ä™dzie]
            sumy_kolorow = [0, 0, 0, 0]
            for kolor in range(1, 5):
                for karta in reka_gracza:
                    if karta.kolor_id == kolor:
                        sumy_kolorow[kolor-1] += 1
            kolor_najwiecej = 0
            for i in range (4):
                if sumy_kolorow[i] > kolor_najwiecej:
                    kolor_najwiecej = i
            if kolor_najwiecej == 0: kolor_wiodacy = "Dzwonki"
            if kolor_najwiecej == 1: kolor_wiodacy = "Serce"
            if kolor_najwiecej == 2: kolor_wiodacy = "Wino"
            if kolor_najwiecej == 3: kolor_wiodacy = u"Ĺ»oĹ‚Ä™dzie"
            print u" Komputer zmieniĹ‚ kolor na ", kolor_wiodacy
            return
        else:
            if karta.kolor == kolor_wiodacy:
                do_wyboru.append(karta)
            elif karta.figura == karta_wiodaca.figura:
                do_wyboru.append(karta)

    if len(do_wyboru) > 0:
        najlepiej_zagrac = do_wyboru[0]
        for karta in do_wyboru:
            if karta.wartosc > najlepiej_zagrac.wartosc:
                najlepiej_zagrac = karta
        reka_komputera.remove(najlepiej_zagrac)
        karta_wiodaca = najlepiej_zagrac
        kolor_wiodacy = karta_wiodaca.kolor
        print u" Komputer zagraĹ‚ ", najlepiej_zagrac.krotka_nazwa

    else:
        if len(talia) >0:
            nastepna_karta = random.choice(talia)
            reka_komputera.append(nastepna_karta)
            talia.remove(nastepna_karta)
            print u" Komputer dobraĹ‚ kartÄ™"
        else:
            print " Komputer jest zablokowany"
            zablokowani += 1
    print u"Komputerowi pozostaĹ‚y %i karty" % (len(reka_komputera))

     
#-------------------------------------
# Main program loop
#-------------------------------------
koniec = False
gracz_razem = komp_razem = 0
while not koniec:
    koniec_partii = False

    zablokowani = 0
    inicjalizacja_kart()
    while not koniec_partii:
        tura_gracza()
        if len(reka_gracza) == 0:
            koniec_partii = True
            print
            print u"WygraĹ‚eĹ›!"
            # wyĹ›wietlamy wynik
            gracz_punkty = 0
            for karta in reka_komputera:
                gracz_punkty += karta.wartosc
            gracz_razem += gracz_punkty
            print u"OtrzymaĹ‚eĹ› %i punktĂłw z kart na rÄ™ce komptera" % gracz_punkty

        if not koniec_partii:
            tura_komputera()
        if len(reka_komputera) == 0:
            koniec_partii = True
            print
            print u"WygraĹ‚ komputer!"
            # wyĹ›wietlamy wynik
            komp_punkty = 0
            for karta in reka_gracza:
                komp_punkty += karta.wartosc
            komp_razem += komp_punkty
            print u"Komputer otrzymaĹ‚ %i punktĂłw z kart na Twojej rÄ™ce" % komp_punkty
        if zablokowani >= 2:
            koniec_partii = True
            print u"Obaj zawodnicy sÄ… zablokowani. KONIEC GRY."
            gracz_punkty = 0
            for karta in reka_komputera:
                gracz_punkty += karta.wartosc
            gracz_razem += gracz_punkty
            komp_punkty = 0
            for karta in reka_gracza:
                komp_punkty += karta.wartosc
            komp_razem += komp_punkty
            print u"OtrzymaĹ‚eĹ› %i punktĂłw z kart na rÄ™ce komptera" % gracz_punkty
            print u"Komputer otrzymaĹ‚ %i punktĂłw z kart na Twojej rÄ™ce" % komp_punkty
    jeszcze_raz = raw_input("Jeszcze jedna partia (T/N)? ")
    if jeszcze_raz.lower().startswith('t'):
        koniec = False
        print "\nZdobyĹ‚eĹ› do tej pory %i punktĂłw" % gracz_razem
        print "a komputer zdobyĹ‚ %i punktĂłw.\n" % komp_razem
    else:
        koniec = True

print u"\n KoĹ„cowy wynik:"
print "Ty: %i Komputer: %i" % (gracz_razem, komp_razem)



