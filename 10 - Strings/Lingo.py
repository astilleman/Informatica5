def hint(gok, antwoord):
    for i in range(0, len(gok)):
        if gok[i] not in antwoord:
            gok = gok[:i] + '.' + gok[i + 1:]
        elif gok[i] == antwoord[i]:
            gok = gok[:i] + gok[i].upper() + gok[i + 1:]
        else:
            gok = gok[:i] + gok[i] + gok[i + 1:]
    return gok

print(hint('zoets', 'zager'))


