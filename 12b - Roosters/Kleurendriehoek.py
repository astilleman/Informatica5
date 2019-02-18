def volgende_rij(lijst):
    next_row = []
    for i in range(1, len(lijst)):
        if lijst[i - 1] == lijst[i]:
            next_row.append(lijst[i])
        elif lijst[i - 1] in 'RY' and lijst[i] in 'RY':
            next_row.append('G')
        elif lijst[i - 1] in 'RG' and lijst[i] in 'RG':
            next_row.append('Y')
        elif lijst[i - 1] in 'GY' and lijst[i] in 'GY':
            next_row.append('R')
    return next_row

#print(volgende_rij(['G', 'G', 'G', 'G', 'G']))
#print(volgende_rij(['Y', 'R', 'G', 'Y', 'Y']))

def driehoek(lijst):
    triangle = [lijst]
    triangle.append(volgende_rij(lijst))
    for i in range(2, len(lijst)):
        triangle.append(volgende_rij(triangle[i - 1]))
    return triangle

#print(driehoek(['G', 'G', 'G', 'G', 'G']))
#print(driehoek(['Y', 'R', 'G', 'Y', 'Y']))

def kleuren(lijst):
    green, red, yellow = 0, 0, 0
    for i in range(len(lijst)):
        for j in range(len(lijst[i])):
            if lijst[i][j] == 'G':
                green += 1
            elif lijst[i][j] == 'R':
                red += 1
            elif lijst[i][j] == 'Y':
                yellow += 1
    return green, red, yellow

#print(kleuren([['G', 'G', 'G', 'G', 'G'], ['G', 'G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G'], ['G']]))
#print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))

'''#betere versie
def driehoek(lijst):
    triangle = [lijst]
    for i in range(1, len(lijst)):
        triangle.append(volgende_rij(triangle[i - 1]))
    return triangle'''