from operator import itemgetter

def bereken_prijs(lijst):

    prijs = 0

    #overloop alle boodschappen

    for item in lijst:
        # telkens het element op index 1 optellen bij de totale prijs
        prijs += item[1]

    return prijs

#print(bereken_prijs([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))


def winkelbriefje(lijst):
    # nieuwe lijst maken
    # eventueel met for i in range(len)
    briefje = []

    #overloop alle boodschappen

    for item in lijst:
        #telkens het element op index 0 aan de nieuwe lijst toevoegen

        briefje.append(item[0])

    return briefje

#print(winkelbriefje([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))

def sorteer(lijst):
    lijst.sort(key=itemgetter(1))
    return lijst


#print([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)])

'''def winkelbriefje(lijst):
    briefje = []
    for i in range(len(lijst)):
        briefje.append(lijst[i][0])
    return briefje'''




