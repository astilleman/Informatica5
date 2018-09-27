# coëfficiënten van x^2, x^1 en x^0
a = float(input('Geef a: '))
b = float(input('Geef b: '))
c = float(input('Geef c: '))

print('a=' , a, ', b =',b, ', c =', c)

#discriminant berekenen
d = (b ** 2) - (4 * a * c)

#discriminant tonen
print(d)
