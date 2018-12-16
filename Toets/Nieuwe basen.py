#invoer
aantal_basen = int(input('Geef het aantal basen: '))
base = str(input('Geef de naam van de base (A/T/G/C): '))
verschillende_basen = base + ' '
reeds_voorkomende_basen = base

#for-lus
for i in range(aantal_basen - 1):
    reeds_voorkomende_basen += base
    base = str(input('Geef de naam van de base (A/T/G/C): '))
    if base not in verschillende_basen:
        verschillende_basen += base + ' '

if len(verschillende_basen) == 2:
    mes = 'De DNA-keting bevat 1 soort base: {}'.format(base)

else:
    mes = 'De DNA-keting bevat {} verschillende soorten basen: {}'.format ((int(len(verschillende_basen) / 2)), verschillende_basen)

#uitvoer
print(mes)





