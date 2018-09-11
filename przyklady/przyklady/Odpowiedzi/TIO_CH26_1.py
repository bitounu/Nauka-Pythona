# TIO_26_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 1, z rozdzia�u 26.

# Sztuczna inteligencja kt�ra jest w stanie pokona� inteligencj� OkreznaSI
class SI:
    def __init__(self):
        self.czyPierwszaTura = True
    def tura(self):
        if self.czyPierwszaTura:
            self.robot.obrotLewo()
            self.czyPierwszaTura = False
        elif self.robot.spojrzPrzedSiebie() == "bot":
            self.robot.atakuj()
        else:
            self.robot.nicNieRob()

