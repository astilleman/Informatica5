def kleur_toevoegen(lijst, kleur):
    if kleur == 'rood':
        lijst[0] += 1
    elif kleur == 'groen':
        lijst[1] += 1
    elif kleur == 'blauw':
        lijst[2] += 1
    return lijst

#print(kleur_toevoegen([3, 0, 8], 'groen'))
#print(kleur_toevoegen([0, 3, 5], 'blauw'))
#print(kleur_toevoegen([9, 2, 4], 'rood'))

def is_wit(lijst):
    return lijst[0] == lijst[1] == lijst[2]

#print(is_wit([2, 2, 2]))
#print(is_wit([1, 3, 5]))

def verf_verzamelen(lijst):
    verflijst = [0, 0, 0]
    i = 0
    while (is_wit(verflijst) is False or verflijst == [0, 0, 0]) and i < len(lijst):
        kleur_toevoegen(verflijst, lijst[i])
        i += 1
    if i <= len(lijst) and is_wit(verflijst):
        aantal = 3 * verflijst[0]
        message = (aantal, verflijst)
    else:
        message = None
    return message

#print(verf_verzamelen(['rood', 'rood', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'groen', 'blauw', 'groen', 'groen', 'groen', 'blauw', 'blauw', 'groen', 'blauw']))
#print(verf_verzamelen(['blauw', 'rood', 'groen', 'blauw', 'groen', 'rood', 'blauw', 'rood', 'blauw', 'rood', 'rood', 'blauw', 'blauw', 'rood', 'groen', 'rood', 'groen']))
#print(verf_verzamelen(['groen', 'groen', 'rood', 'groen', 'rood', 'groen', 'groen', 'rood', 'blauw', 'groen', 'groen', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'blauw', 'rood']))

'''#als niet gegeven 3 elementen
def is_wit(lijst):
    mes = True
    i = 0
    while i < len(lijst) - 1 and mes is True:
        if lijst[i] != lijst[i + 1]:
            mes = False
        i += 1
    return mes
'''