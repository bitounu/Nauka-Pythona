m = 10
g = 2
i = 0
j = 10
s = int(input('Podaj liczbe: '))
def los(s,i,j):
    i = i+1
    if i <= j:
        a = s * g % m
        print "%d ," % a
        los(a)

los(s)

