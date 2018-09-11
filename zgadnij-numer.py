import random

proby = 6
granica = 20
tajna_liczba = random.randint(1, granica)

print "******************************************************"
print "*     Twoim zadaniem jest odgadnac tajna liczbe.     *"
print "*     To liczba miedzy 1  a %s                       *" % granica
print "*     Zgadywac mozesz %d razy                         *" % proby
print "******************************************************"

for proba in range(proby):
    liczba = int(input('Podaj liczbe: '))

    if liczba < tajna_liczba:
        print 'Tajna liczba jest wieksza...'
    elif liczba > tajna_liczba:
        print 'Tajna liczba jest mniejsza...'
    else:
        print('')
        print('Bingo! Tajna liczba to ', tajna_liczba)
        print('Odgadles za ', proby, 'podejsciem.')

        break

if liczba != tajna_liczba:
    print('')
    print('Niestety, wyczerpales juz wszystkie mozliwosci')
    print('Tajna liczba to ', tajna_liczba)
