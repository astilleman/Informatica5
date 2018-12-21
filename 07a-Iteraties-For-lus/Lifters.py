#invoer
n = int(input('Geef het aantal lifters: '))
hoogste_voorlopige_score1 = 0
hogere_score2 = 0

#berekening
for i in range(n // 2):
    s1 = float(input('Geef de score van de lifter: '))
    if s1 > hoogste_voorlopige_score1:
        hoogste_voorlopige_score1 = s1

for i in range((n // 2), n):
    if hogere_score2 == 0:
        s2 = float(input('Geef de score van de lifter: '))
        if s2 > hoogste_voorlopige_score1:
            hogere_score2 = s2

if hogere_score2 == 0:
    hogere_score2 = s2

#uitvoer
print(hogere_score2)

'''11
0.9325
0.8133
0.9770
0.4468
0.0421
0.4733
0.6340
0.1222
0.5770
0.9067
0.4965
'''

