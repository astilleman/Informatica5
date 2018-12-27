#invoer
n = int(input('Geef een getal: '))
echte_delers = '1 '
som = 1

#berekening
for i in range(2, n):
    if n % i == 0:
        echte_delers += '{} '.format(i)
        som += i

if n == som and n != 1:
    mes = '{} is een perfect getal en de delers zijn {}'.format(n, echte_delers)
else:
    mes = '{} is geen perfect getal'.format(n)

#uitvoer
print(mes)