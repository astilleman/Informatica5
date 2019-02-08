def hoogtemeters(lijst):
    nieuwe_lijst = []
    for i in range(0, len(lijst) - 1):
        nieuwe_lijst.append(lijst[i + 1] - lijst[i])

    return nieuwe_lijst

#print(hoogtemeters([822, 61, 347, 234, 883, 336]))

def dalen_en_stijgen(lijst):
    stijgen, dalen = 0, 0
    for hoogte in lijst:
        if hoogte >= 0:
            stijgen += hoogte
        else:
            dalen += hoogte

    return abs(dalen), stijgen

#print(dalen_en_stijgen([0]))


