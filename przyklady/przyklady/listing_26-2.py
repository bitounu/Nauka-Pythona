# Listing 26-2
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# SI Bitwy pythonów - drugie podejœcie do pokonania OkreznaSI

# Zwróæ uwagê, ¿e nie jest kompletny program Pythona
#  Jest to modu³ wywo³ywany przez program Bitwa pythonów
# Zapisz ten plik pod dowolna nazw¹ - np. "bardziejrozbudowanasi.py"
#  I przetestuj go w walce przeciwko okreznasi


class SI:
    def __init__(self):
        pass
    def tura(self):
        if self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
        else:
            self.idzKierunek(self.robot.znajdzWroga()[0])
    def idzKierunek(self,polozenieWroga):
        mojePolozenie = self.robot.polozenie
        delta = (polozenieWroga[0]-mojePolozenie[0],
                 polozenieWroga[1]-mojePolozenie[1])
        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                kierunekWroga = 3   # Skieruj siê w lewo
            else:
                kierunekWroga = 1   # Skieruj siê w prawo
        else:
            if delta[1] < 0:
                kierunekWroga = 0   # Skieruj siê do góry
            else:
                kierunekWroga = 2   # Skieruj siê w dó³
        if self.robot.kierunek == kierunekWroga:
            self.robot.idzDoPrzodu()
        else:
            wymaganeSkretyLewo = (self.robot.kierunek - kierunekWroga) % 4
            if wymaganeSkretyLewo <= 2:
                self.robot.obrotLewo()
            else:
                self.robot.obrotPrawo()
