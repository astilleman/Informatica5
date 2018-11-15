#bewerking
totale_prijs = 0
prijs = float(input('Prijs van het product: '))
while prijs > 0:
    totale_prijs += prijs
    prijs = float(input('Prijs van het product: '))

mes = 'De totale prijs is € {:.2f}'.format(totale_prijs)

#uitvoer
print(mes)
