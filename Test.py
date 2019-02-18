def volgende_rij(lijst):
    next_row = []
    for i in range(1, len(lijst)):
        if lijst[i] == lijst[i - 1]:
            next_row.append(lijst[i])
        elif lijst[i] in 'GR' and lijst[i - 1] in 'GR':
            next_row.append('Y')
        elif lijst[i] in 'GY' and lijst[i - 1] in 'GY':
            next_row.append('R')
        elif lijst[i] in 'YR' and lijst[i - 1] in 'YR':
            next_row.append('G')
    return next_row

#print(volgende_rij(['G', 'G', 'G', 'G', 'G']))
#print(volgende_rij(['Y', 'R', 'G', 'Y', 'Y']))

def driehoek(lijst):
    triangle = [lijst]
    for i in range(1, len(lijst)):
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

print(kleuren([['G', 'G', 'G', 'G', 'G'], ['G', 'G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G'], ['G']]))
print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))

