#invoer
d = float(input('Geef de initiële populatiedichtheid: '))
r = float(input('Geef de vruchtbaarheidsparameter: '))
s = int(input('Geef  het aantal tijdsstappen: '))
t = 0
mes = '{}\n'.format(d)

#berekening
for i in range(s - 1):
    t += 1
    d = r * d * (1 - d)
    mes += '{}\n'.format(d)

#uitvoer
print(mes)
