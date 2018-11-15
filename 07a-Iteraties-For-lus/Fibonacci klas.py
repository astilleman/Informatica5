n = int(input('Hoeveelste getal van Fibonacci: '))

vorige, huidige = 1, 1

for i in range(n-2):
    vorige, huidige = huidige, huidige + vorige
    #met hulp

print(huidige)