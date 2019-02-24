def beweeg(tuple, teken):
    coördinaten = list(tuple)
    if teken == '<':
        coördinaten[0] -= 1
    elif teken == '>':
        coördinaten[0] += 1
    elif teken == '^':
        coördinaten[1] += 1
    elif teken == 'v':
        coördinaten[1] -= 1
    mes = (coördinaten[0], coördinaten[1])

    return mes

#print(beweeg((-6, -6), '<'))
#print(beweeg((7, 3), '^'))

def teruggekeerd(pijltjes):
    mes = False
    if pijltjes[0] == '<' and pijltjes[1] == '>':
        mes = True
    elif pijltjes[0] == '>' and pijltjes[1] == '<':
        mes = True
    elif pijltjes[0] == 'v' and pijltjes[1] == '^':
        mes = True
    elif pijltjes[0] == '^' and pijltjes[1] == 'v':
        mes = True
    return mes

#print(teruggekeerd(['^', 'v']))
#print(teruggekeerd(['>', 'v']))


def laatste_levende_positie(pijltjeslijst):
    i = 0
    aantal = 1
    positie = beweeg((0, 0), pijltjeslijst[i])
    while teruggekeerd(pijltjeslijst[i:i + 2]) is False and i < len(pijltjeslijst) - 2:
        positie = beweeg(positie, pijltjeslijst[i + 1])
        i += 1
        aantal += 1
    if teruggekeerd(pijltjeslijst[i:i + 2]) is False:
        positie = beweeg(positie, pijltjeslijst[i + 1])
        aantal += 1

    mes = (aantal, positie[0], positie[1])

    return mes, len(pijltjeslijst)


print(laatste_levende_positie(['>', '<', '^']))
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))