def ik_heb_gemoord(lijst, moordenaar):
    if len(lijst) > 1:
        index_moordenaar = lijst.index(moordenaar)
        if index_moordenaar < len(lijst) - 2:
            index_slachtoffer = index_moordenaar + 1
            index_nieuw_slachtoffer = index_moordenaar + 2
            lijst.remove(lijst[index_slachtoffer])
        elif index_moordenaar == len(lijst) - 2:
            index_slachtoffer = index_moordenaar + 1
            index_nieuw_slachtoffer = 0
            lijst.remove(lijst[index_slachtoffer])
        elif index_moordenaar == len(lijst) - 1:
            index_slachtoffer = 0
            index_nieuw_slachtoffer = 1
            lijst.remove(lijst[index_slachtoffer])
    else:
        index_nieuw_slachtoffer = 0

    return lijst[index_nieuw_slachtoffer], lijst

#print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))
#print(ik_heb_gemoord(['jan'],'jan'))

def ik_ben_vermoord(lijst, slachtoffer):
    if len(lijst) > 1:
        index_slachtoffer = lijst.index(slachtoffer)
        if index_slachtoffer != len(lijst) - 1:
            index_nieuw_slachtoffer = index_slachtoffer + 1
            lijst.remove(lijst[index_slachtoffer])
        else:
            index_nieuw_slachtoffer = 0
            lijst.remove(lijst[index_slachtoffer])
    else:
        index_nieuw_slachtoffer = 0

    return lijst[index_nieuw_slachtoffer], lijst

print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))
print(ik_ben_vermoord(['jan'],'jan'))