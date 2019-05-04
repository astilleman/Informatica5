ruilmarkt = {'goud': {'wol', 'steen', 'erts'}, 'wol': {'hout', 'steen', 'erts'}, 'erts': {'hout', 'steen'}, 'steen': {'hout', 'graan'}}

def wisselen_mogelijk(ruilmarkt, grondstof, verzamelde_grondstoffen):
    set_grondstoffen = set(verzamelde_grondstoffen)
    return ruilmarkt.get(grondstof).issubset(set_grondstoffen)

#print(wisselen_mogelijk(ruilmarkt, 'steen', ['wol', 'erts']))
#print(wisselen_mogelijk(ruilmarkt, 'wol', ['graan', 'erts', 'steen', 'steen', 'erts', 'erts', 'hout', 'goud']))

def bereken_ruilmiddelen(ruilmarkt, gewenste_grondstoffen):
    dictionary_grondstoffen = {}
    for grondstof in gewenste_grondstoffen:
        ruilmiddelen = ruilmarkt.get(grondstof)
        for ruilmiddel in ruilmiddelen:
            if ruilmiddel in dictionary_grondstoffen:
                dictionary_grondstoffen[ruilmiddel] += 1
            else:
                dictionary_grondstoffen[ruilmiddel] = 1
    return dictionary_grondstoffen

#print(bereken_ruilmiddelen(ruilmarkt, ['wol']))
#print(bereken_ruilmiddelen(ruilmarkt, ['goud', 'erts', 'erts']))

def wisselen(ruilmarkt, grondstof, verzamelde_grondstoffen):
    if wisselen_mogelijk(ruilmarkt, grondstof, verzamelde_grondstoffen) is True:
        nodige_grondstoffen = list(ruilmarkt.get(grondstof))
        for nodige_grondstof in nodige_grondstoffen:
            verzamelde_grondstoffen.remove(nodige_grondstof)
        verzamelde_grondstoffen.append(grondstof)
    return verzamelde_grondstoffen

#print(wisselen(ruilmarkt, 'steen', ['wol', 'erts']))
#print(wisselen(ruilmarkt, 'wol', ['graan', 'erts', 'steen', 'steen', 'erts', 'erts', 'hout', 'goud']))

