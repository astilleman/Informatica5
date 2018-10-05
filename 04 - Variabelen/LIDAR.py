#gegevens
c = 299792458
n = 1.000277

#invoer
t = int(input('Geef tijd: ')) * (10 ** (-9))

#berekening
d = (c * t) / (2 * n)

#uitvoer
uitvoer = str(d) + ' meter'
print(uitvoer)