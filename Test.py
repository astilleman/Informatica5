from operator import itemgetter

def bereken_prijs(lijst):
    prijs = 0
    for item in lijst:
        prijs += item[1]
    return prijs

#print(bereken_prijs([('Crocky Zout', 1.39)]))
#print(bereken_prijs([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))

def bereken_prijs(lijst):
    prijs = 0
    for i in range(len(lijst)):
        prijs += lijst[i][1]
    return prijs

#print(bereken_prijs([('Crocky Zout', 1.39)]))
#print(bereken_prijs([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))

def winkelbriefje(lijst):
    briefje = []
    for item in lijst:
        briefje.append(item[0])
    return briefje

#print(winkelbriefje([('Crocky Zout', 1.39)]))
#print(winkelbriefje([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))

def winkelbriefje(lijst):
    briefje = []
    for i in range(len(lijst)):
        briefje.append(lijst[i][0])
    return briefje

#print(winkelbriefje([('Crocky Zout', 1.39)]))
#print(winkelbriefje([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))

def sorteer(lijst):
    lijst.sort(key=itemgetter(1))
    return lijst

#print(sorteer([('Crocky Zout', 1.39)]))
#print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))


