"""
Nazwa SI: Okr�na SI

Autor: Carter

Strategia: Porusza si� dooko�a pola bityw. Atakuje przeciwnika znajduj�cego si� na �cie�ce.

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
