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
                 polozenieWroga[1]- mojePolozenie[1])
        if abs(delta[0]) > abs(delta[1]):
            if delta[0] < 0:
                kierunekWroga = 3
            else:
                kierunekWroga = 1
        else:
            if delta[1] < 0:
                kierunekWroga = 0
            else:
                kierunekWroga = 2
        if self.robot.kierunek == kierunekWroga:
            self.robot.idzDoPrzodu()
        else:
            wymaganeSkretyLewo = (self.robot.kierunek - kierunekWroga) % 4
            if wymaganeSkretyLewo <= 2:
                self.robot.obrotLewo()
            else:
                self.robot.obrotPrawo()
