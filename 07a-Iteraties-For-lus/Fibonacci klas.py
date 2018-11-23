n = int(input('Hoeveelste getal van Fibonacci: '))

vorige, huidige = 1, 1

for i in range(n-2):
    vorige, huidige = huidige, huidige + vorige
    #met hulp

print(huidige)

##############################################################zelf met hulponbekende

'''invoer
n = int(input('Geef het nde getal in de rij van Fibanacci: '))
vorige_term, huidige_term = 1, 1
for i in range(n - 2):
    hulp = vorige_term
    vorige_term = huidige_term
    huidige_term = hulp + huidige_term

print(huidige_term)'''