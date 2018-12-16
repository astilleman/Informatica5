#invoer
snelheid_stijn = int(input('Geef de snelheid van Stijn: '))
snelheid_kaat = int(input('Geef de snelheid van Kaat: '))
x = int(input('De afstand tussen Stijn en Kaat: '))
t = 1

#while-lus
while x > (snelheid_kaat * t) + (snelheid_stijn * t):
    t += 1

#formattering
mes = 'Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(t)

#uitvoer
print(mes)
