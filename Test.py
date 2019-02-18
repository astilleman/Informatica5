def ik_heb_gemoord(lijst, moordenaar):
    if len(lijst) > 1:
        #slachtoffer schrappen
        index_moordenaar = lijst.index(moordenaar)
        index_slachtoffer = (index_moordenaar + 1) % len(lijst)
        lijst[index_slachtoffer:index_slachtoffer + 1] = []

        #nieuwe opdracht moordenaar
        index_moordenaar = lijst.index(moordenaar)
        index_nieuw_slachtoffer = (index_moordenaar + 1) % len(lijst)
    else:
        index_nieuw_slachtoffer = 0

    return lijst[index_nieuw_slachtoffer], lijst

print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))
print(ik_heb_gemoord(['jan'],'jan'))

def ik_ben_vermoord(lijst, slachtoffer):
    if len(lijst) > 1:

        #slachtoffer schrappen
        index_slachtoffer = lijst.index(slachtoffer)
        lijst[index_slachtoffer:index_slachtoffer + 1] = []

        #nieuwe opdracht moordenaar
        index_nieuw_slachtoffer = index_slachtoffer % len(lijst)


    else:
        index_nieuw_slachtoffer = 0

    return lijst[index_nieuw_slachtoffer], lijst

print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))
print(ik_ben_vermoord(['jan'],'jan'))