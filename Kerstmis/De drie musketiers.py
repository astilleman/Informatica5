#invoer
t = int(input('Geef het aantal rijen van het rechthoekig rooster: '))

#berekening
horizontale_buren, verticale_buren, musketiers, tekst, buren, aantal_buren1, aantal_buren2, buurtje = '', '', '', '', '', 0, '', ''
for i in range(t):
    regel = input('Geef een regel: ')
    tekst += regel
for i in range(len(tekst)):
    if i == 0:
        horizontale_buren += tekst[i + 1]
    elif 1 <= i < len(tekst) and (i + 1) % len(regel) != 0 and i % len(regel) != 0:
        horizontale_buren += tekst[i - 1] + tekst[i + 1]
    elif i % len(regel) == 0:
        horizontale_buren += tekst[i + 1]
    elif (i + 1) % len(regel) == 0:
        horizontale_buren += tekst[i - 1]
    elif i == len(tekst):
        horizontale_buren += tekst[i - 1]

    if len(regel) <= i < len(tekst) - len(regel):
        verticale_buren += tekst[i - len(regel)] + tekst[i + len(regel)]
    elif i < len(regel):
        verticale_buren += tekst[i + len(regel)]
    elif i >= len(tekst) - len(regel):
        verticale_buren += tekst[i - len(regel)]
    buren = horizontale_buren + verticale_buren
    aantal_buren1 = buren.count(buren[0])
    aantal_buren2 = buren.count(buren[1])
    if aantal_buren1 == 3:
        if 65 <= ord(buren[0]) <= 90 or 97 <= ord(buren[0]) <= 122:
            musketiers += tekst[i].upper()
        elif 48 <= ord(buren[0]) <= 57:
            musketiers += tekst[i].lower()
        else:
            musketiers += tekst[i]
    elif aantal_buren2 == 3:
        if 65 <= ord(buren[1]) <= 90 or 97 <= ord(buren[1]) <= 122:
            musketiers += tekst[i].upper()
        elif 48 <= ord(buren[1]) <= 57:
            musketiers += tekst[i].lower()
        else:
            musketiers += tekst[i]
    horizontale_buren, verticale_buren = '', ''


#uitvoer
print(musketiers)

