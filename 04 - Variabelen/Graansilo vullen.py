#import pi
from math import pi

#invoer
b = float(input('Geef breedte:' ))
l = float(input('Geef lengte: '))
c = float(input('Geef hoeveelheid graan per kubieke meter: ')) * (10 ** (-4))
r = float(input('Geef straal graansilo: '))
h = float(input('Geef hoogte graansilo: '))

#berekening
aantal_graansilos = int((((c * (l * b)) / (pi * (r ** 2) *h)) + 0.999) // 1)
#hoogte_oogst_laatste_graansilo =
hoogte_laatste_graansilo = float((((c * (l * b)) / (pi * (r ** 2) *h)) - ((((c * (l * b)) / (pi * (r ** 2) *h)) - 0.001) // 1)) * h)


print(aantal_graansilos)
print(hoogte_laatste_graansilo)


#503.3 623.4 5.5 2.1 5.6
#3.1415926535897931 16 100000 4 10