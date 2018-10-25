from math import sqrt
#invoer
x = float(input('Geef een getal x: '))

#bewerking
if x < 2:
    print('{:.2f} ∉ dom(f)'.format(x))

elif x == 2:
    print('2.00 is nulpunt van f')

else:
    print('f({:.2f}) = {:.2f}'.format(x, sqrt(x - 2)))