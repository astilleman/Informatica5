#invoer
opeenvolging_aminozuren = input('Geef de opeenvolging van de aminozuren in het eiwit: ')
m = int(input('Geef een getal: '))
n = int(input('Geef een groter getal dan m: '))

#berekening
aantal_afwijkingen, plaats_afwijking, naam_afwijkingen = 0, '', ''
cijfers = '0123456789'
for i in range(n):
    afwijking = input('Geef een afwijking van het eiwit: ')
    for j in afwijking:
        if j in cijfers:
            plaats_afwijking += j
        else:
            naam_afwijkingen += j
    if opeenvolging_aminozuren[int(plaats_afwijking) - 1] in naam_afwijkingen:
        aantal_afwijkingen += 1
    plaats_afwijking, naam_afwijkingen = '', ''

#print(plaats_afwijking)
#print(naam_afwijkingen)

if aantal_afwijkingen >= m:
    diagnose = 'positief'
else:
    diagnose = 'negatief'

#formattering
message = '{} ({})'.format(diagnose, aantal_afwijkingen)

#uitvoer
print(message)

###########################################################################################################################

#invoer
aminozuren = input('Geef de reeks opeenvolgende aminozuren in het eiwit: ')
m = int(input('Geef een getal m: '))
n = int(input('Geef een getal die groter dan of gelijk is aan n: '))

#berekening
plaats_afwijking, naam_afwijking, aantal_afwijkingen = '', '', 0
for i in range(n):
    afwijking = input('Geef een afwijking van het eiwit: ')

    for i in range(len(afwijking)):
        if afwijking[i] in '0123456789':
            plaats_afwijking += afwijking[i]
        else:
            naam_afwijking += afwijking[i]

    if aminozuren[int(plaats_afwijking) - 1] in naam_afwijking:
        aantal_afwijkingen += 1

    if aantal_afwijkingen >= m:
        diagnose = 'positief'
    else:
        diagnose = 'negatief'
    naam_afwijking, plaats_afwijking = '', ''

#formattering
message = '{}({})'.format(diagnose, aantal_afwijkingen)

#uitvoer
print(message)