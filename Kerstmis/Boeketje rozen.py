#invoer
a = int(input('Geef het totaal aantal rode en witte rozen in een boeket: '))
b = int(input('Geef het totaal aantal witte en blauwe rozen in een boeket: '))
c = input('Is het aantal blauwe en rode rozen groter/kleiner dan het totaal aantal witte en blauwe rozen (>/<): ')

#berekening

blauwe_rozen, witte_rozen, rode_rozen = 0, 0, 0
if c == '<':
    witte_rozen = a // 2 + 1
    rode_rozen = a - witte_rozen
    blauwe_rozen = b - witte_rozen

elif c == '>':
    rode_rozen = a // 2 + 1
    witte_rozen = a - rode_rozen
    blauwe_rozen = b - witte_rozen

if blauwe_rozen < 2 or witte_rozen < 2 or rode_rozen < 2:
    if c == '<':
        witte_rozen = b // 2 + 1
        blauwe_rozen = b - witte_rozen
        rode_rozen = a - witte_rozen

    elif c == '>':
        blauwe_rozen = b // 2 + 1
        witte_rozen = b - blauwe_rozen
        rode_rozen = a - witte_rozen


if blauwe_rozen == 1:
    blauwe_rozen += 1
    witte_rozen -= 1

if rode_rozen == 1:
    rode_rozen += 1
    witte_rozen -= 1

if witte_rozen == 1:
    witte_rozen += 1
    rode_rozen -= 1
    blauwe_rozen -= 1

message = '{}\n{}\n{}'.format(blauwe_rozen, witte_rozen, rode_rozen)

#uitvoer
print(message)



