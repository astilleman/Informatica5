#invoer
temperatuur = input('Geef de warmst waargenomen temperatuur: ')
zomerse_dagen = 0
tropische_dagen = 0

#while-lus
while temperatuur != 'stop':
    temp = float(temperatuur)
    temperatuur = input('Geef de warmst waargenomen temperatuur: ')
    if temp >= 30:
        tropische_dagen += 1
        zomerse_dagen += 1
    elif temp >= 25:
        zomerse_dagen += 1
    elif zomerse_dagen >= 5 and tropische_dagen >= 3:
        zomerse_dagen = zomerse_dagen
        tropische_dagen = tropische_dagen
    else:
        zomerse_dagen, tropische_dagen = 0, 0


if zomerse_dagen >= 5 and tropische_dagen >= 3:
    mes = 'hittegolf'
else:
    mes = 'geen hittegolf'

#uitvoer
print(mes)