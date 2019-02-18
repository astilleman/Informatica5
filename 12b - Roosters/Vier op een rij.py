def printbaar_rek(lijst):
    rek = ''
    lijst.reverse()
    for element in lijst:
        for j in range(len(element)):
            rek += element[j]
        if element != lijst[len(lijst) - 1]:
            rek += '\n'
    return rek

#print(printbaar_rek([['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))
#print(printbaar_rek([['R', 'R', 'R', 'R', 'G'], ['G', 'G', 'R', 'G', 'R'], ['O', 'G', 'O', 'O', 'O'], ['O', 'R', 'O', 'O', 'O']]))

def speel(kleur, rij, lijst):
    spel = 'niet gedaan'
    i = 0
    while i < len(lijst) and spel != 'gespeeld':
        if lijst[i][rij] == 'O':
            lijst[i][rij] = kleur
            spel = 'gespeeld'
        i += 1
    return lijst

#print(speel('G',1,[['R', 'R', 'R', 'R', 'G'], ['G', 'G', 'R', 'G', 'R'], ['O', 'G', 'O', 'O', 'O'], ['O', 'R', 'O', 'O', 'O']]))
#print(speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))

'''#stel de elementen zijn ook nog van rechts naar links gestopt
def printbaar_rek(lijst):
    lijst.reverse()
    for item in lijst:
        item.reverse()
    return lijst
    #andere mogelijkheid
def printbaar_rek(lijst):
lijst.reverse()
rek = ''
for i in range(len(lijst)):
    for j in range(len(lijst[i])):
        rek += lijst[i][j]
    if lijst[i] != lijst[len(lijst) - 1]:
        rek += '\n'
return rek'''

