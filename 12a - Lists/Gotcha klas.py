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