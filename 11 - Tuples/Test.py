gewesten = ('Vlaanderen', 'Wallonië', 'Brussel')

for gewest in gewesten:
    print(gewest.upper())

for i in range(len(gewesten)):
    print(gewesten[i].upper())

#gewesten[0] = 'Fladern'
#in een tuple kan je geen element vervangen zoals in een string

#gewesten += 'Zeeuws-Vlaanderen'
#niets aanhangen, eens de tuple bestaan onveranderlijk

print(gewesten[0:2])
print(gewesten[1:])
print(gewesten[-1])
#1 element niet meer tussen haakjes in een tuple
print(gewesten[0:5])
print(gewesten[5])
#ook index out of range

