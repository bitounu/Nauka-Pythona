# Listing 26-1
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# SI Bitwy pythonów - pierwsze podejœcie do pokonania OkreznaSI

# Zwróæ uwagê, ¿e nie jest kompletny program Pythona
#  Jest to modu³ wywo³ywany przez program Bitwa pythonów
# Zapisz ten plik pod dowolna nazw¹ - np. "lepszanizokreznasi.py"
#  I przetestuj go w walce przeciwko okreznasi


class SI:
    def __init__(self):
        self.biezaceZadanie = "przod"
    def tura(self):
        if self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
        elif self.robot.spojrzPrzedSiebie() == "sciana":
            self.robot.obrotPrawo()
            self.biezaceZadanie = "obrotPrawo"
        elif self.biezaceZadanie == "obrotPrawo":
            self.robot.obrotPrawo()
            self.biezaceZadanie = "przod"
        else:
            self.robot.idzDoPrzodu()
