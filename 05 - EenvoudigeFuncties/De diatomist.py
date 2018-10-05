#invoer
r1 = float(input('Geef kleine straal: '))
r2 = float(input('Geef grote straal: '))

#berekening maximum aantal kleine cirkels
n = int((0.83 * ((r2 ** 2) / (r1 ** 2))) - 1.9)

#berekening bedekkingsgraad grotere cirkel
from math import pi
opp_kleine_cirkels = n * ((r1 ** 2) * pi)
opp_grote_cirkel = (r2 ** 2) * pi
bedekkingsgraad = ((opp_kleine_cirkels) / (opp_grote_cirkel)) * 100

#formattering op 2 cijfers na komma
bedekkingsgraad_op_honderdste = '{:.2f}'.format(bedekkingsgraad)

#uitvoer
uitvoer = str(n) + ' kleine cirkels bedekken ' + str(bedekkingsgraad_op_honderdste) + '% van de grote cirkel'
print(uitvoer)