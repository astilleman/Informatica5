ruilmarkt = {'goud': {'wol', 'steen', 'erts'}, 'wol': {'hout', 'steen', 'erts'}, 'erts': {'hout', 'steen'}, 'steen': {'hout', 'graan'}}

def bereken_ruilmiddelen(ruilmarkt, gewenst):
    grondstof_dictionary = {}
    for grondstof in gewenst:
        ruilmiddelen = ruilmarkt.get(grondstof)
        for ruilmiddel in ruilmiddelen:
            if ruilmiddel in grondstof_dictionary:
                grondstof_dictionary[ruilmiddel] += 1
            else:
                grondstof_dictionary[ruilmiddel] = 1
    return grondstof_dictionary

#print(bereken_ruilmiddelen(ruilmarkt, ['wol']))
#print(bereken_ruilmiddelen(ruilmarkt, ['goud', 'erts', 'erts']))

def inventaris(verzameld):
    bezit = {}
    for grondstof in verzameld:
        if grondstof in bezit:
            bezit[grondstof] += 1
        else:
            bezit[grondstof] = 1
    return bezit

def wisselen_mogelijk(ruilmarkt, gewenst, verzameld):
    nodig = bereken_ruilmiddelen(ruilmarkt, gewenst)
    bezit = inventaris(verzameld)
    mes = True
    for grondstof in nodig:
            if grondstof not in bezit or nodig.get(grondstof) > bezit.get(grondstof) or mes is False:
                mes = False
    return mes
#print(wisselen_mogelijk(ruilmarkt, ['erts', 'erts'] ,['steen', 'hout', 'wol', 'steen', 'steen', 'hout']))
#print(wisselen_mogelijk(ruilmarkt, ['erts', 'goud'] ,['wol', 'steen', 'erts', 'hout', 'wol']))


def wisselen(ruilmarkt, grondstoffen, verzameld):
    if wisselen_mogelijk(ruilmarkt, grondstoffen, verzameld) is True:
        for grondstof in grondstoffen:
            nodige_grondstoffen = ruilmarkt.get(grondstof)
            for nodige_grondstof in nodige_grondstoffen:
                verzameld.remove(nodige_grondstof)
            verzameld.append(grondstof)
    return verzameld

print(wisselen(ruilmarkt, ['erts', 'erts'],['steen', 'hout', 'wol', 'steen', 'steen', 'hout'] ))
#print(wisselen(ruilmarkt, ['erts', 'goud'], ['graan', 'erts', 'steen', 'steen', 'erts', 'erts', 'hout', 'goud']))