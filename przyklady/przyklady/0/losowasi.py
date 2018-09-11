"""
Nazwa SI: Losowa SI

Autor: Carter

Strategia:
Przemieszcza robota w sposób losowy.
Atakuje robota znajdującego się przed sobą.
"""

import random

class SI:
    def __init__(self):
        # tutaj umieścić kod, jaki ma wykonać SI przed rozpoczęciem walki.        
        pass
    def tura(self):
        if self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
            return
        else:
            random.choice([self.robot.obrotLewo,self.robot.obrotPrawo,self.robot.idzDoPrzodu,self.robot.idzDoPrzodu])()
