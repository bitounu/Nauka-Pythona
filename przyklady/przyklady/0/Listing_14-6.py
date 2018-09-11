# Listing_14-6.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Klasa HotDog zawierająca metody podgrzej(), dodaj_dodatek() i __str__()

class HotDog:
    def __init__(self):
        self.podgrzanie_poziom = 0
        self.podgrzanie_tekst = "Surowy"
        self.dodatki = []
    # Definicja metody __str__()
    # która wyświetla dodatki do hotdoga
    def __str__(self):
        komunikat = "hot dog"
        if len(self.dodatki) > 0:
            komunikat = komunikat + " z "
        for i in self.dodatki:
            komunikat = komunikat+i+", "
        komunikat = komunikat.strip(", ")
        komunikat = self.podgrzanie_tekst + " " + komunikat + "."
        return komunikat
    
    def podgrzej(self, czas):
        self.podgrzanie_poziom = self.podgrzanie_poziom + czas
        if self.podgrzanie_poziom > 8:
            self.podgrzanie_tekst = "Spalony"
        elif self.podgrzanie_poziom > 5:
            self.podgrzanie_tekst = "Mocno podgrzany"
        elif self.podgrzanie_poziom > 3:
            self.podgrzanie_tekst = "Średnio podgrzany"
        else:
            self.podgrzanie_tekst = "Surowy"
            
    def dodaj_dodatek(self, dodatek):
        self.dodatki.append(dodatek)


mojHotDog = HotDog()        # tworzymy instancję

# sprawdzamy, czy wszystko działa
print mojHotDog
print "Podgrzewamy parówkę przez 4 minuty..."
mojHotDog.podgrzej(4)
print mojHotDog
print "Podgrzewamy parówkę jeszcze przez 3 minuty..."
mojHotDog.podgrzej(3)
print mojHotDog
print "Co się stanie, jeśli będziemy podgrzewać parówkę jeszcze przez 10 minut?"
mojHotDog.podgrzej(10)
print mojHotDog
print "Teraz dodamy do hot doga jakieś dodatki."
mojHotDog.dodaj_dodatek("ketchup")
mojHotDog.dodaj_dodatek("musztarda")
print mojHotDog
