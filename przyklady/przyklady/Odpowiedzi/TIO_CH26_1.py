# TIO_26_1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# OdpowiedŸ do zadania praktycznego 1, z rozdzia³u 26.

# Sztuczna inteligencja która jest w stanie pokonaæ inteligencjê OkreznaSI
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

