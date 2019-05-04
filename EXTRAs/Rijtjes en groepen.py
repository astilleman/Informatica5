def groep(stenen):
    stenen = list(stenen)
    i = 1
    mes = True
    cijfer = stenen[0][0]
    kleur = stenen[0][1]
    while i < len(stenen) and mes is True:
        if stenen[i][0] != cijfer or stenen[i][1] == kleur:
            mes = False
        i += 1
    return mes

#print(groep(['4R', '4B', '4G', '4Z']))
#print(groep({'6B', '7B', '8B', '9B', '10B'}))
#print(groep(('11R', '2B', '7G', '2B', '9Z')))


def rijtje(stenen):
    stenen = list(stenen)
    stenen_lengte2 = []
    stenen_lengte3 = []
    sorted_stenen = []
    for steen in stenen:
        if len(steen) == 2:
            stenen_lengte2.append(steen)
        else:
            stenen_lengte3.append(steen)
    stenen_lengte2.sort()
    stenen_lengte3.sort()
    sorted_stenen.extend(stenen_lengte2)
    sorted_stenen.extend(stenen_lengte3)
    i = 1
    mes = True
    if len(sorted_stenen[0]) == 2:
        kleur = sorted_stenen[0][1]
    else:
        kleur = sorted_stenen[0][2]
    while i < len(sorted_stenen) and mes is True:
        if len(sorted_stenen[i]) == 2:
            if int(sorted_stenen[i][0]) != int(sorted_stenen[i-1][0]) + 1 or sorted_stenen[i][1] != kleur:
                mes = False
        elif len(sorted_stenen[i]) == 3 and len(sorted_stenen[i - 1]) == 2:
            if int(sorted_stenen[i][0:2]) != int(sorted_stenen[i-1][0]) + 1 or sorted_stenen[i][2] != kleur:
                mes = False
        else:
            if int(sorted_stenen[i][0:2]) != int(sorted_stenen[i -1][0:2]) + 1 or sorted_stenen[i][2] != kleur:
                mes = False
        i += 1
    return mes


#print(rijtje(['4R', '4B', '4G', '4Z']))
#print(rijtje({'6B', '7B', '8B', '9B', '10B'}))
#print(rijtje(('11R', '2B', '7G', '2B', '9Z')))