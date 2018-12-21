#invoer
n = int(input('Hoeveel gebouwen staan er precies naast elkaar? '))
eerste_gebouw, eerste_hoogte = '', 0
groter_gebouw, grotere_hoogte = '', 0
vorige_hoogte = 0

#berekening
for i in range(n):
    gebouw = input('Wat is de naam van het gebouw? ')
    hoogte = int(input('Wat is de hoogte van het gebouw?(in m) '))
    if eerste_hoogte == 0:
        eerste_gebouw += gebouw
        eerste_hoogte += hoogte
        grotere_hoogte = eerste_hoogte
        mes = '{} is zichtbaar van het gelijkvloers tot {} meter.\n'.format(eerste_gebouw, eerste_hoogte)
    elif hoogte > grotere_hoogte:
        vorige_hoogte = grotere_hoogte
        grotere_hoogte = hoogte
        groter_gebouw = gebouw
        mes += '{} is zichtbaar van {} meter tot {} meter.\n'.format(groter_gebouw, vorige_hoogte, grotere_hoogte)

#uitvoer
print(mes)
