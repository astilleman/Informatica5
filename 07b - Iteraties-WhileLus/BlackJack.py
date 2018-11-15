#bewerking
totaal_kaarten = 0
kaart = int(input('Geef een kaart: '))
extra_kaart = 1
mes = ''

while (totaal_kaarten + kaart) < 21 and extra_kaart != 0:
    totaal_kaarten += kaart
    kaart = int(input('Geef een kaart: '))
    if kaart == 0:
        extra_kaart = 0

if totaal_kaarten < 21 and extra_kaart == 0:
    mes = 'Voorzichtig gespeeld ({})'.format(totaal_kaarten)

elif (totaal_kaarten + kaart) == 21:
    mes = 'Gewonnen!'

elif (totaal_kaarten + kaart) > 21:
    mes = 'Verbrand ({})'.format(totaal_kaarten + kaart)

#uitvoer
print(mes)