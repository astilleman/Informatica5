#invoer
t = int(input('Geef een tijdstip: '))
stappen = 0

#berekening
for i in range(1, (t + 1)):
    if i % 2 != 0:
        stappen += i + 1
    else:
        stappen -= (i // 2)

#uitvoer
print(stappen)

