#start
n = int(input('Geef het aantal getallen: '))
som, maximum  = 0, 0

#berekeningen
for i in range(n):
    getallen = int(input('Getal: '))
    som += getallen
    if getallen > maximum:
        maximum = getallen
    elif maximum == 0:
        maximum = getallen
    else:
        maximum = maximum


gemiddelde = (1/n) * som

#formattering
mes = 'Het grootste getal is {} en het gemiddelde is {:.2f}'.format(maximum, gemiddelde)

#uitvoer
print(mes)







