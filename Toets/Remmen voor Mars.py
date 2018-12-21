#invoer
gewenste_landsnelheid = int(input('Geef de gewenste landsnelheid (in m/s): '))
raketsnelheid = int(input('Geef de raketsnelheid (in m/s): '))
aantal_rembewegingen = 0

#while-lus
while raketsnelheid > gewenste_landsnelheid:
    aantal_rembewegingen += 1
    raketsnelheid *= 0.7

#message
mes = 'na {} rembewegingen is de snelheid {:.2f}'.format(aantal_rembewegingen, raketsnelheid)

#uitvoer
print(mes)
