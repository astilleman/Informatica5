#invoer
doden = int(input('Geef het aantal overleden gevangenen na 24 uur: '))

#invoer met for-lus
genoemde_letters = ''
for i in range(doden):
    letter_gevangene = input('Geef de positieletter van de dode: ')
    genoemde_letters += letter_gevangene

#binair stelsel
reeks = 'ABCDEFGHIJ'
for j in range(0, len(reeks)):
    if reeks[j] in genoemde_letters:
        reeks = reeks[:j] + '1' + reeks[j + 1:]
    else:
        reeks = reeks[:j] + '0' + reeks[j + 1:]

#berekening flesnummer
flesnummer = 0
for i in range(0, 10):
    if int(reeks[i]) == 1:
        flesnummer += 2 ** i

#formattering
message = 'Fles #{} is vergiftigd.'.format(flesnummer)

#uitvoer
print(message)

#####################################################################################################"
#invoer
n = int(input('Aantal overleden gevangenen: '))

#berekening
genoemde_letters = ''
reeks_gevangenen = 'JIHGFEDCBA'
for i in range(n):
    letter_gevangene = input('Geef de letter van de overleden gevangene: ')
    genoemde_letters += letter_gevangene

#berekening binaire omzetting
binaire_reeks_gevangenen = ''
for i in range(len(reeks_gevangenen)):
    if reeks_gevangenen[i] in genoemde_letters:
        binaire_reeks_gevangenen = binaire_reeks_gevangenen[:i] + '1' + binaire_reeks_gevangenen[i + 1:]
    else:
        binaire_reeks_gevangenen = binaire_reeks_gevangenen[:i] + '0' + binaire_reeks_gevangenen[i + 1:]

print(binaire_reeks_gevangenen)

#berekening flesnummer
fles = 0
for i in range(len(binaire_reeks_gevangenen)):
    if binaire_reeks_gevangenen[i] == '1':
        fles += 2 ** (len(binaire_reeks_gevangenen) - 1 - i)


#formattering

message = 'Fles #{} is vergiftigd.'.format(fles)

#uitvoer
print(message)