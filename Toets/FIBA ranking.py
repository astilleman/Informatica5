#invoer
pt = int(input('Geef het aantal punten van de thuisploeg: '))
pu = int(input('Geef het aantal punten van de uitploeg: '))

#berekening behaalde punten thuisploeg en uitploeg
if pt > pu and abs(pt - pu) < 10:
    punten_thuisploeg = 600
    punten_uitploeg = 400
elif pt < pu and abs(pt - pu) < 10:
    punten_thuisploeg = 400
    punten_uitploeg = 600
elif pt > pu and 10 <= abs(pt - pu) < 20:
    punten_thuisploeg = 700
    punten_uitploeg = 300
elif pt < pu and 10 <= abs(pt - pu) < 20:
    punten_thuisploeg = 300
    punten_uitploeg = 700
elif pt > pu:
    punten_thuisploeg = 800
    punten_uitploeg = 200
else:
    punten_thuisploeg = 200
    punten_uitploeg = 800

#effect thuisvoordeel uitwissen
punten_thuisploeg -= 70
punten_uitploeg += 70

#uitvoer
print('thuisploeg: {:.2f}'.format(punten_thuisploeg))
print('  uitploeg: {:.2f}'.format(punten_uitploeg))