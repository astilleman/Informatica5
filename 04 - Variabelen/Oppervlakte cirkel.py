pi = 3.14159

#invoer
r = float(input('Geef straal: '))

#berekening
opp_cirkel = pi * (r ** 2)

#De oppervlakte van een cirkel met straal 4.2222 is 56.0050396044156
#uitvoer
#spaties voor en na is!
resultaat = 'De oppervlakte van een cirkel met straal '
resultaat += str(r) + ' is ' + str(opp_cirkel)

print(resultaat)