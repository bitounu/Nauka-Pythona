# pythonbattle.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Program BitwaPytonow uruchamia kod dwóch walcz¹cych ze sob¹ SI.
# Program tworzy siatkê bêd¹c¹ polem bitwy i rozpoczyna pojedynek.

import pygame #ASCII/PYGAME
import time
pygame.init() #ASCII/PYGAME

class BladTury(Exception):
    """ Wyj¹tek informuj¹cy o tym, ¿e robot ma zamiar poruszyæ siê nie w swojej turze """    
    def __init__(self,nazwaBota):
        self.nazwaBota = nazwaBota
    def __str__(self):
        return "Robot "+self.nazwaBota+" mia³ zamiar wywo³aæ funckjê nie w swojej turze."

class BladPrzegranegoRobota(Exception):
    """ Wyj¹tek informuj¹cy o tym, ¿e robor ma zamiar wykonac ruch po przegraniu walki """

    def __init__(self,nazwaBota):
        self.nazwaBota = nazwaBota
    def __str__(self):
        return "Robot " +self.nazwaBota+ " mia³ zamiar wywo³aæ funkcjê po przegraniu walki."


class Robot:
    
    """ Robot reprezentuj¹cy gracza
    Wartoœci informuj¹ce o obrocie
    0: góra
    1: prawo
    2: dó³
    3: lewo

    Uwaga: wszystkie metody o nazwach rozpoczynaj¹cych siê od znaku _ s¹ metodami prywatnymi.
    Nie wowo³uj ich pod ¿adnym pozorem. """
    def __init__(self,nazwa,si,polozenie,kierunek):
        self.nazwa = nazwa
        self.si = si
        si.robot = self
        self.polozenie = polozenie
        self.kierunek = kierunek
        self.zdrowie = 100
    def _miejsceNaWprost(self):
        if self.kierunek == 0:
            return (self.polozenie[0],self.polozenie[1]-1)
        elif self.kierunek == 1:
            return (self.polozenie[0]+1,self.polozenie[1])
        elif self.kierunek == 2:
            return (self.polozenie[0],self.polozenie[1]+1)
        elif self.kierunek == 3:
            return (self.polozenie[0]-1,self.polozenie[1])
    def _pobierzMiejsce(self,miejsce):
        global pole
        if miejsce == self.polozenie:
            return "ja"
        else:
            for i in pole:
                if i.polozenie == miejsce:
                    return "bot"
        if miejsce[0]<1:
            return "sciana"
        elif miejsce[1]<1:
            return "sciana"
        elif miejsce[0]>10:
            return "sciana"
        elif miejsce[1]>10:
            return "sciana"
        else:
            return "czysto"
    def _idzDoPrzodu(self):
        if self._pobierzMiejsce(self._miejsceNaWprost()) == "czysto":
            self.polozenie = self._miejsceNaWprost()
            return "sukces"
        else:
            return self._pobierzMiejsce(self._miejsceNaWprost())
    def _cofnijSie(self):
        self._obrotLewo()
        self._obrotLewo()
        if self._pobierzMiejsce(self._miejsceNaWprost()) == "czysto":
            self.polozenie = self._miejsceNaWprost()
            self._obrotPrawo()
            self._obrotPrawo()
            return "sukces"
        else:
            result = self._pobierzMiejsce(self._miejsceNaWprost())
            self._obrotPrawo()
            self._obrotPrawo()
            return result
    def _obrotLewo(self):
        self.kierunek -= 1
        self.kierunek %= 4
        return "sukces"
    def _obrotPrawo(self):
        self.kierunek += 1
        self.kierunek %= 4
        return "sukces"
    def _atakuj(self):
        global pole
        for i in pole:
            if i.polozenie == self._miejsceNaWprost():
                i.otrzymajObrazenia(10)
                return "sukces"
        return self._pobierzMiejsce(self._miejsceNaWprost())
    def _przedRuchem(self):
        """ Sprawdzam, czy robot ma zamiar wykonaæ ruch nie w swojej turze lub gdy zosta³ ju¿ pokonany. """        
        global stan
        if (stan != self.nazwa) and (stan != "wygrana"):
            raise BladTury,self.nazwa
        elif stan == "wygrana":
            raise BladPrzegranegoRobota,self.nazwa
    def _poRuchu(self):
        """ Kiedy robot wykona ju¿ ruch, zmieniamy stan gry tak, aby ruch móg³ wykonaæ drugi robot. """     
        global pole, stan
        if stan == self.nazwa:
            for i in pole:
                if i.nazwa != self.nazwa:
                    stan = i.nazwa
    def obliczWspolrzedne(self,odleglosc=1,kierunek=None,polozenie=None):
        """ Pomocnicza funkcja obliczaj¹ca po³o¿enie.
        Zwraca wspó³rzêdne wskazanego miejsca."""
        if kierunek == None:
            kierunekDoSprawdzenia = self.kierunek
        else:
            kierunekDoSprawdzenia = kierunek
        if polozenie == None:
            zwracanePolozenie = self.polozenie
        else:
            zwracanePolozenie = polozenie
        kierunekDoSprawdzenia %= 4
        for i in range(odleglosc):
            if kierunekDoSprawdzenia == 0:
                zwracanePolozenie= (zwracanePolozenie[0],zwracanePolozenie[1]-1)
            elif kierunekDoSprawdzenia == 1:
                zwracanePolozenie= (zwracanePolozenie[0]+1,zwracanePolozenie[1])
            elif kierunekDoSprawdzenia == 2:
                zwracanePolozenie= (zwracanePolozenie[0],zwracanePolozenie[1]+1)
            elif kierunekDoSprawdzenia == 3:
                zwracanePolozenie= (zwracanePolozenie[0]-1,zwracanePolozenie[1])
        return zwracanePolozenie
    def spojrzPrzedSiebie(self):
        "Sprawdza, co znajduje siê przed robotem"        
        return self.spojrzNaMiejsce(self.obliczWspolrzedne())
    def spojrzNaMiejsce(self,miejsce):
        "Sprawdza, co znajduje siê w okreœlonym miejscu"
        return self._pobierzMiejsce(miejsce)
    def otrzymajObrazenia(self,obrazenia):
        "Nie wywo³uj tej funkcji. Zadaje ona robotowi okreœlone obra¿enia"        
        global stan, pole
        self.zdrowie -= obrazenia
        if self.zdrowie <= 0:
            stan = "wygrana"
    def atakuj(self):
        "Atak"
        self._przedRuchem()
        wynik = self._atakuj()
        self._poRuchu()
        return wynik
    def cofnijSie(self):
        "Cofniêcie siê"
        self._przedRuchem()
        wynik = self._cofnijSie()
        self._poRuchu()
        return wynik
    def idzDoPrzodu(self):
        "Przesuniêcie siê do przodu"
        self._przedRuchem()
        wynik = self._idzDoPrzodu()
        self._poRuchu()
        return wynik
    def obrotLewo(self):
        "Obrót w lewo"
        self._przedRuchem()
        wynik = self._obrotLewo()
        self._poRuchu()
        return wynik
    def nicNieRob(self):
        "Robot nic nie robi i koñczy turê"        
        self._przedRuchem()
        wynik = "sukces"
        self._poRuchu()
        return wynik
    def obrotPrawo(self):
        "Obrót w prawo"
        self._przedRuchem()
        wynik = self._obrotPrawo()
        self._poRuchu()
        return wynik
    def znajdzWroga(self):
        "Sprawdza w którym miejscu znajduj sie siê robot przeciwnika"        
        global pole
        for i in pole:
            if i.nazwa != self.nazwa:
                return i.polozenie, i.kierunek

def rysujPoleBitwy(bot1, bot2):
    """ Rysuje pole bitwy za pomoc¹ znaków ASCII.
    Aby w grze narysowaæ pole bitwy za pomoc¹ znaków ASCII,
    zamieñ wszystkie wywo³ania funkcji rysujPoleBitwyPygame t¹ funkcj¹.
    
    Funkcja nie rysuje czerwonych i niebieskich kwadratów. """
    poleBitwy = ""
    for wiersz in range(12):
        for kolumna in range(12):
            if wiersz in [0,11]:
                #rysuj œcianê
                poleBitwy += "--"
            elif kolumna in [0,11]:
                #rysuj œcianê
                poleBitwy += "||"
            elif (kolumna,wiersz) == bot1.polozenie:
                #rysuj robota 1
                poleBitwy += ["^",">","V","<"][bot1.kierunek]+"1"
            elif (kolumna,wiersz) == bot2.polozenie:
                #rysuj robota 2
                poleBitwy += ["^",">","V","<"][bot2.kierunek]+"2"
            else:
                poleBitwy += "  "
        poleBitwy += "\n"
    print poleBitwy
    # wyœwietl wskaŸniki ¿ycia
    print "¯ycie robota 1:",bot1.zdrowie
    print "¯ycie robota 2:",bot2.zdrowie

def rysujPoleBitwyPygame(bot1, bot2):
    """ Rysuje pole bitwy za pomoc¹ Pygame"""    
    global stan, czerwone_pola, niebieskie_pola, bot1rys, bot2rys, nazwaCzcionka, si1nazwa, si2nazwa

    # pobieramy powierzchniê ekranu
    ekran = pygame.display.get_surface()    
    
    # otwieramy okno Pygame, je¿eli nie zosta³o ono jeszcze otwarte
    if ekran == None:
        ekran = pygame.display.set_mode((640,480))
    # czyœcimy ekran
    ekran.fill((0,0,0))
    # rysujemy kolorowe kwadraty
    for i in czerwone_pola:
        pygame.draw.rect(ekran,(64,0,0),((  (i[0]-1)*48,(i[1]-1)*48  ),(48,48)))
    for i in niebieskie_pola:
        pygame.draw.rect(ekran,(0,0,64),(((i[0]-1)*48,(i[1]-1)*48),(48,48)))
    # rysujemy linie siatki
    for i in range(1,10):
        pygame.draw.line(ekran,(50,50,50),(0,i*48),(480,i*48),5)
        pygame.draw.line(ekran,(50,50,50),(i*48,0),(i*48,480),5)
    
    # pobieramy po³o¿enie robotów na ekranie
    bot1pos = ((bot1.polozenie[0]-1)*48,(bot1.polozenie[1]-1)*48)
    bot2pos = ((bot2.polozenie[0]-1)*48,(bot2.polozenie[1]-1)*48)
    # rysujmey na ekranie roboty
    ekran.blit(pygame.transform.rotate(bot1rys,-90*bot1.kierunek),bot1pos)
    ekran.blit(pygame.transform.rotate(bot2rys,-90*bot2.kierunek),bot2pos)
    # wyœwietlamy na ekranie nazwy robotów
    ekran.blit(nazwaCzcionka.render(si1nazwa,True,(255,0,0),(0,0,0)),(480,0))
    ekran.blit(nazwaCzcionka.render(si2nazwa,True,(0,0,255),(0,0,0)),(480,40))
    # wyœwietlamy na ekranie paski ¿ycia robotów
    pygame.draw.rect(ekran,(0,255,0),((480,20),(int(bot1.zdrowie*160/100.0),10)))
    pygame.draw.rect(ekran,(0,255,0),((480,60),(int(bot2.zdrowie*160/100.0),10)))
    pygame.display.flip()
    # je¿eli gra siê zakoñczy...
    if stan == "wygrana":
        uruchomiony = True
        # czekamy, a¿ u¿ytkownik zamknie okno
        while uruchomiony:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    uruchomiony = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        uruchomiony = False
    else:
        # w przeciwnym razie miêdzy klatkami wprowadzamy opóŸnienie
        time.sleep(0.1)

# tworzymy obiekt Font
nazwaCzcionka = pygame.font.Font(None,25)
# pobieramy nazwy zawodników
si1nazwa = raw_input("WprowadŸ SI gracza czerwonego: ")
si2nazwa = raw_input("WprowadŸ SI gracza niebieskiego: ")
# w sposób dynamiczny ³adujemy modu³y zawieraj¹ce SI robotów
si1 = __import__(si1nazwa) 
si2 = __import__(si2nazwa)
# tworzymy dwa obiekty robotów wyposa¿onych w okreœlon¹ SI
pole = [Robot("czerwony",si1.SI(),(10,5),3),Robot("niebieski",si2.SI(),(1,5),1)]
czerwone_pola = []
niebieskie_pola = []
stan = "czerwony"

pygame.display.set_mode((640,480))
# ³adujemy grafikê i rysujemy pole bitwy
bot1rys = pygame.image.load("DozerRed.png").convert_alpha()
bot2rys = pygame.image.load("DozerBlue.png").convert_alpha()
rysujPoleBitwyPygame(pole[0],pole[1]) #ASCII/PYGAME


liczbaTur = 0

while stan != "wygrana":
    # kolorowe kwadraty
    if not (pole[0].polozenie[0],pole[0].polozenie[1]) in czerwone_pola:
        czerwone_pola.append((pole[0].polozenie[0],pole[0].polozenie[1]))
        while (pole[0].polozenie[0],pole[0].polozenie[1]) in niebieskie_pola:
            niebieskie_pola.remove((pole[0].polozenie[0],pole[0].polozenie[1]))
    if not (pole[1].polozenie[0],pole[1].polozenie[1]) in niebieskie_pola:
        niebieskie_pola.append((pole[1].polozenie[0],pole[1].polozenie[1]))
        while (pole[1].polozenie[0],pole[1].polozenie[1]) in czerwone_pola:
            czerwone_pola.remove((pole[1].polozenie[0],pole[1].polozenie[1]))
    
    rysujPoleBitwyPygame(pole[0],pole[1]) #ASCII/PYGAME
    for i in pole:
        try: # zapobiegamy zawieszeniu gry, gdy zawiedzie kod SI
            i.si.tura()
        except Exception,e:
            print i.nazwa," zg³osi³ b³¹d:"
            print e
    liczbaTur += 1
    if liczbaTur == 1000:
        # je¿eli gra trwa wiêcej ni¿ ok. 1.6 min., przerywamy rozgrywkê        
        stan = "pat"
        break
    
# po raz ostatni kolorowe kwadraty
if not (pole[0].polozenie[0],pole[0].polozenie[1]) in czerwone_pola:
    czerwone_pola.append((pole[0].polozenie[0],pole[0].polozenie[1]))
    while (pole[0].polozenie[0],pole[0].polozenie[1]) in niebieskie_pola:
        niebieskie_pola.remove((pole[0].polozenie[0],pole[0].polozenie[1]))
if not (pole[1].polozenie[0],pole[1].polozenie[1]) in niebieskie_pola:
    niebieskie_pola.append((pole[1].polozenie[0],pole[1].polozenie[1]))
    while (pole[1].polozenie[0],pole[1].polozenie[1]) in czerwone_pola:
        czerwone_pola.remove((pole[1].polozenie[0],pole[1].polozenie[1]))
if stan == "pat":
    rysujPoleBitwyPygame(pole[0],pole[1])#ASCII/PYGAME
    print "Skoñczy³y siê tury!"
    # je¿eli robot ma wiêcej zdrowia, wygrywa    
    if pole[0].zdrowie > pole[1].zdrowie:
        print "Czerwony wygrywa!"
    elif pole[1].zdrowie > pole[0].zdrowie:
        print "Niebieski wygrywa!"
    else:
        # w przeciwnym razie, wygrywa ten, kto ma najwiêcej kwadratów w soim kolorze        
        print "Wykryto sytuacjê patow¹!"
        print "Zlicznie liczby kolorowych pól..."
        time.sleep(2) # chwila przerwy dla nadania sytuacji dramatyzmu...
        if len(czerwone_pola) > len(niebieskie_pola):
            print "Wygra³ Czerwony z",len(czerwone_pola),"polami!"
            print "(Niebieski mia³",len(niebieskie_pola),"pól)"
        elif len(czerwone_pola) < len(niebieskie_pola):
            print "Wygra³ Niebieski z",len(niebieskie_pola),"polami!"
            print "(Czerwony mia³",len(czerwone_pola),"pól)"
        else:
            print "Remis! Obaj zawodnicy maj¹ po",len(czerwone_pola),"pól."
    stan = "wygrana"
else:
    # wyœwietlamy kto wygra³
    if pole[0].zdrowie > pole[1].zdrowie:
        print "Wygrywa Czerwony z ",pole[0].zdrowie," punktami zdrowia!"
    if pole[1].zdrowie > pole[0].zdrowie:
        print "Wygrywa Niebieski z",pole[1].zdrowie," punktami zdrowia!"
rysujPoleBitwyPygame(pole[0],pole[1])     #ASCII/PYGAME
pygame.quit() #ASCII/PYGAME
