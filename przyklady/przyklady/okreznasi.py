"""
Nazwa SI: Okrê¿na SI

Autor: Carter

Strategia: Porusza siê dooko³a pola bityw. Atakuje przeciwnika znajduj¹cego siê na œcie¿ce.

"""


class SI:
    def __init__(self):
        self.isFirstTurn = True
    def tura(self):
        if self.isFirstTurn:
            self.robot.obrotPrawo()
            self.isFirstTurn = False
        elif self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
        elif self.robot.spojrzPrzedSiebie()== "sciana":
            self.robot.obrotLewo()
        else:
            self.robot.idzDoPrzodu()
