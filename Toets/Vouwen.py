#invoer
dikte = int(input('Geef de dikte van het blad papier (in mm): '))
afstand = int(input('Geef de afstand van de aarde tot bijvoorbeeld een hemellichaam (in mm): '))
aantal_vouwen = 0

#while-lus
while afstand > dikte:
    aantal_vouwen += 1
    dikte *= 2

#message
mes = 'Na {} keer vouwen bedraagt de dikte van het papier {} mm.'.format(aantal_vouwen, dikte)

#uitvoer
print(mes)