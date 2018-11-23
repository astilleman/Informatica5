aantal = int(input('aantal'))
grootste = int(input('getal: '))
som = grootste

for i in range(aantal - 1):
    getal = int(input('getal: '))
    som += getal
    if getal > grootste:
        grootste = getal

print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootste, som/aantal))

##########################################################################zelf

'''aantal = int(input('Geef het aantal getallen: '))
getal = int(input('Geef een geheel getal: '))
grootste = getal
som = getal

for i in range(aantal - 1):
    getal = int(input('Geef een geheel getal: '))
    som += getal
    if getal > grootste:
        grootste = getal
print(som)
mes = 'Het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootste, (som /aantal))

#uitvoer
print(mes)'''