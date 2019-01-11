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