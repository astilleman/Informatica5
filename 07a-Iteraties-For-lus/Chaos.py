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

'''0.1
4
60
Uitvoer:

0.1
0.36000000000000004
0.9216
... (54 regels) ...
0.977464119602946
0.08811205796713474
0.32139329283172413'''