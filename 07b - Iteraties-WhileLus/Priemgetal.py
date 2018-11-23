#klas

getal = int(input('getal: '))

#zolang je het kan delen door 2, 3, 4 is het allicht een priemgetal

deler = 2

while getal % deler != 0 and getal != 1:
#while getal / deler != getal //deler:
# of kleiner dan wortel
    deler += 1
    #print(deler)

if deler == getal:
    mes = 'priemgetal'
else:
    mes = 'geen priemgetal'

print(mes)
