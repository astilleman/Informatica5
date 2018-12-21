#invoer
startkapitaal = int(input('Geef het startkapitaal van de speler: '))
ingezette_bedrag = input('Geef het ingezette bedrag van de speler: ')
bedrag = startkapitaal

#while-lus
str_ingezette_bedrag = ingezette_bedrag
if str_ingezette_bedrag == 'alles':
    ingezette_bedrag = bedrag
else:
    ingezette_bedrag = int(ingezette_bedrag)

while str_ingezette_bedrag != 'stop' and bedrag > 0 and bedrag >= ingezette_bedrag:
    kleur_inzet = input('Geef de kleur waarop de speler inzet: ')
    kleur_landing = input('Geef de kleur waarop het balletje landt: ')
    if kleur_landing == kleur_inzet:
        bedrag += ingezette_bedrag
    else:
        bedrag -= ingezette_bedrag
    ingezette_bedrag = input('Geef het ingezette bedrag van de speler: ')
    str_ingezette_bedrag = ingezette_bedrag
    if str_ingezette_bedrag == 'alles':
        ingezette_bedrag = bedrag
    elif str_ingezette_bedrag == 'stop':
        str_ingezette_bedrag = 'stop'
    else:
        ingezette_bedrag = int(ingezette_bedrag)

if str_ingezette_bedrag == 'stop' or bedrag <= 0:
    mes = 'Je eindigt met {} dollar.'.format(bedrag)
elif ingezette_bedrag > bedrag:
    mes = 'Je kunt geen {} dollar inzetten als je maar {} dollar hebt.'.format(ingezette_bedrag, bedrag)

#uitvoer
print(mes)


'''444100
218586
rood
rood
499771
zwart
zwart
alles
zwart
zwart
alles
rood
rood
alles
rood
zwart
68700
zwart
zwart
alles
rood
rood
246100
zwart
rood
stop'''