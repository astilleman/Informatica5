#invoer
serienummer = int(input('Geef het serienummer van de Duitse tank: '))
aantal_serienummers = 0
maximaal_serienummer = serienummer

#while-lus
while serienummer > 0:
    aantal_serienummers += 1
    serienummer = int(input('Geef het serienummer van de Duitse tank: '))
    if serienummer > maximaal_serienummer:
        maximaal_serienummer = serienummer

#berekening aantal geproduceerde tanks
aantal = (((aantal_serienummers + 1) * maximaal_serienummer) / aantal_serienummers) - 1

#message
mes = 'Het aantal geproduceerde tanks wordt geschat op {}.'.format(round(aantal))

#uitvoer
print(mes)