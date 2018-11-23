#invoer
h = int(input('Geef een van nul verschillend natuurlijk getal: '))
getal = h
som = 0

while getal > 0:
    som += getal % 10
    getal //= 10

if h % som == 0 or h < 10:
    mes = '{} is een Harshadgetal'.format(h)

else:
    mes = '{} is geen Harshadgetal'.format(h)

#uitvoer
print(mes)

