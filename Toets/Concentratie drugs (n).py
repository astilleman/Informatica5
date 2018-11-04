from math import pi

#invoer
t = float(input('Geef aantal uren sinds de opname van de dosis XTC: '))

#berekening
c = ((pi * t)/(pow(t, 2) + 2))

#uitvoer
uitvoer = print(round(c, 4))