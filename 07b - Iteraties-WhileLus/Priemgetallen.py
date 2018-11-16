#berekening
getal = int(input('Geef een getal: '))
extra_getal = getal
mes = ''

for i in range(2, getal):
    if getal % i == 0:
        extra_getal = getal % i

if getal != extra_getal or getal == 1:
    mes =  '{} is geen priemgetal'.format(getal)

else:
    mes = '{} is een priemgetal'.format(getal)

#uitvoer
print(mes)