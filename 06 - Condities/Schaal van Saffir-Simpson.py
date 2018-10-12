#invoer
x = int(input('Geef een windsnelheid: '))

#berekening
if 119 <= x <= 153:
    print('categorie 1')
elif 154 <= x <= 177:
    print('categorie 2')
elif 178 <= x <= 209:
    print('categorie 3')
elif 210 <= x <= 249:
    print('categorie 4')
elif x >= 250:
    print('categorie 5')
else:
    print('geen orkaan')


