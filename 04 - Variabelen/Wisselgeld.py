a = 100
b = 50
c = 20
d = 10
e = 5
f = 2
g = 1

#input
bedrag_in_eurocent = int(input('Geef bedrag in eurocent: '))

#tussenberekening
h = bedrag_in_eurocent // a
i = (bedrag_in_eurocent - (h * a)) // b
j = (bedrag_in_eurocent - (h * a) - (i * b)) // c
k = (bedrag_in_eurocent - (h * a) - (i * b) - (j * c)) // d
l = (bedrag_in_eurocent - (h * a) - (i * b) - (j * c) - (k * d)) // e
m = (bedrag_in_eurocent - (h * a) - (i * b)- (j * c) - (k * d) - (l * e)) // f
n = (bedrag_in_eurocent - (h * a) - (i * b)- (j * c) - (k * d) - (l * e) - (m * f)) // g

#berekening
aantal_muntstukken = h + i + j + k + l + m + n

#resultaat in zin
resultaat = str(bedrag_in_eurocent) + ' cent kan je omwisselen in '
resultaat += str(aantal_muntstukken) + ' muntstukken'
print(resultaat)