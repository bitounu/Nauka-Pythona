"""
Nazwa SI: Okrężna SI

Autor: Carter

Strategia: Porusza się dookoła pola bityw. Atakuje przeciwnika znajdującego się na ścieżce.

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
