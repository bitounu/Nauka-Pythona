"""
Nazwa SI: Losowa SI

Autor: Carter

Strategia:
Przemieszcza robota w spos�b losowy.
Atakuje robota znajduj�cego si� przed sob�.
"""

import random

class SI:
    def __init__(self):
        # tutaj umie�ci� kod, jaki ma wykona� SI przed rozpocz�ciem walki.        
        pass
    def tura(self):
        if self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
            return
        else:
            random.choice([self.robot.obrotLewo,self.robot.obrotPrawo,self.robot.idzDoPrzodu,self.robot.idzDoPrzodu])()
