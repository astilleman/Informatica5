def ik_heb_gemoord(lijst, moordenaar):
    #slachtoffer schrappen
    index_moordenaar = lijst.index(moordenaar)
    index_slachtoffer = (index_moordenaar + 1) % len(lijst)
    #index_slachtoffer = (lijst.index(moordenaar) + 1) % len(lijst)

    lijst[index_slachtoffer:index_slachtoffer + 1] = []


    #nieuw doel aan de moordenaar geven
    index_moordenaar = lijst.index(moordenaar)
    index_nieuw_doel = (index_moordenaar + 1) % len(lijst)
    #len(lijst) is eentje minder lang geworden

    return lijst, lijst[index_nieuw_doel]


print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))

#zelf thuis op deze manier gedaan
def ik_ben_vermoord(lijst, slachtoffer):

    if len(lijst) > 1:
        #nieuwe opdracht moordenaar
        index_slachtoffer = lijst.index(slachtoffer)
        index_nieuw_slachtoffer = (index_slachtoffer + 1) % len(lijst)

        #slachtoffer schrappen
        lijst[index_slachtoffer: index_slachtoffer + 1] = []
    else:
        index_nieuw_slachtoffer = 0

    return lijst[index_nieuw_slachtoffer], lijst

#print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))
#print(ik_ben_vermoord(['jan'],'jan'))

'''#denk juister
def ik_ben_vermoord(lijst, slachtoffer):
    if len(lijst) > 1:
        
        #slachtoffer schrappen
        index_slachtoffer = lijst.index(slachtoffer)
        lijst[index_slachtoffer:index_slachtoffer + 1] = []

        #nieuwe opdracht moordenaar
        index_nieuw_slachtoffer = index_slachtoffer % len(lijst)


    else:
        index_nieuw_slachtoffer = 0

    return lijst[index_nieuw_slachtoffer], lijst'''