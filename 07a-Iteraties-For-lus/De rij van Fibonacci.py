#start
n = int(input('Geef een getal: '))
term_1, term_2 = 1, 1

#berekening
if n == 1 or n == 2:
    rij_van_Fibonacci = 1

else:
    for i in range(n - 1):
        term_1, term_2 = term_2, term_1 + term_2
        rij_van_Fibonacci = term_1


#uitvoer
print(rij_van_Fibonacci)

