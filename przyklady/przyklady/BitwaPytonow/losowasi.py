"""
Nazwa SI: Losowa SI

Autor: Carter

Strategia:
Przemieszcza robota w sposób losowy.
Atakuje robota znajduj¹cego siê przed sob¹.
"""

import random

class SI:
    def __init__(self):
        # tutaj umieœciæ kod, jaki ma wykonaæ SI przed rozpoczêciem walki.        
        pass
    def tura(self):
        if self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
            return
        else:
            random.choice([self.robot.obrotLewo,self.robot.obrotPrawo,self.robot.idzDoPrzodu,self.robot.idzDoPrzodu])()
