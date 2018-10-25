#invoer
dv = float(input('Geef de verkeersdichtheid van het vrachtvervoer: '))
vv = float(input('Geef de snelheid van het vrachtverkeer: '))
da = float(input('Geef de verkeersdichtheid van het personenvervoer: '))
va = float(input('Geef de snelheid van de de personenwagens: '))

#berekening kans op file
pv = min(((vv *dv ) / 40), 1)
pa = min(((va *da ) / 40), 1)

#kleurcode bepalen
if min(pv, pa) > 0.7:
    kleur = 'zwart'
elif max(pv, pa) > 0.7 and abs(pv - pa) < 0.2:
    kleur = 'rood'
elif abs(pv - pa) > 0.7:
    kleur = 'geel'
else:
    kleur = 'groen'

#uitvoer
print(kleur)