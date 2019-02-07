'''def dubbels(tekst):
    nieuwe_lijst = []
    nieuwe_lijst = tekst[0]
    for i in range(1, len(tekst)):
        if tekst[i] != tekst[i - 1]:
            nieuwe_lijst += tekst[i]

    return nieuwe_lijst

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))


#count elk element in lijst en als het meer dan 1 keer voorkomt is het een dubbel
# neem element en vergelijk met allen andere (lus in lus)
# sorteer lijst en kijk of 2 of 3 of 4 of ... maal hetzelfde element na elkaar zit
# 2 laatste gaan niet!

def dubbels(tekst):
    nieuwe_lijst = []
    for i in range(len(tekst)):
        dub = tekst.count(tekst[i])
        nieuwe_lijst.append(tekst[i])


    return nieuwe_lijst



print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris'])'''

def dubbels(lijst):

    lijst_dubbels = []

    for item in lijst:

        if lijst.count(item) > 1 and item not in lijst_dubbels:

            lijst_dubbels.append(item)

    return lijst_dubbels

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))