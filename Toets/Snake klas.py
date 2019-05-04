def teruggekeerd(richtingen):
    richtingen.sort()
    return richtingen == ['<', '>'] or richtingen == ['^', 'v']

def laatste_levende_positie(kliks):

    x, y = beweeg((0, 0), kliks[0])
    i = 1

    while i < len(kliks) and not teruggekeerd([kliks[i-1], kliks[i]]):
        x, y = beweeg((x, y), kliks[i])

