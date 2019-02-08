def ik_heb_gemoord(opdrachtenlijst, moordenaar):
    if opdrachtenlijst.index(moordenaar) in range(0, len(opdrachtenlijst) - 2):
        nieuw_slachtoffer = opdrachtenlijst[(opdrachtenlijst.index(moordenaar) + 2)]
        opdrachtenlijst.remove(opdrachtenlijst[opdrachtenlijst.index(moordenaar) + 1])
    elif opdrachtenlijst.index(moordenaar) == len(opdrachtenlijst) - 2:
        nieuw_slachtoffer = opdrachtenlijst[0]
        opdrachtenlijst.remove(opdrachtenlijst[len(opdrachtenlijst) - 1])
    elif opdrachtenlijst.index(moordenaar) == len(opdrachtenlijst) - 1 and len(opdrachtenlijst) > 1:
        nieuw_slachtoffer = opdrachtenlijst[1]
        opdrachtenlijst.remove(opdrachtenlijst[0])
    else:
        nieuw_slachtoffer = opdrachtenlijst[0]

    return nieuw_slachtoffer, opdrachtenlijst

#print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'piet'))

def ik_ben_vermoord(opdrachtenlijst, slachtoffer):
    if opdrachtenlijst.index(slachtoffer) != len(opdrachtenlijst) - 1:
        nieuw_slachtoffer = opdrachtenlijst[(opdrachtenlijst.index(slachtoffer) + 1)]
        opdrachtenlijst.remove(opdrachtenlijst[opdrachtenlijst.index(slachtoffer)])
    elif opdrachtenlijst.index(slachtoffer) == len(opdrachtenlijst) - 1 and len(opdrachtenlijst) > 1:
        nieuw_slachtoffer = opdrachtenlijst[0]
        opdrachtenlijst = opdrachtenlijst[0:len(opdrachtenlijst) - 1]
    else:
        nieuw_slachtoffer = opdrachtenlijst[0]

    return nieuw_slachtoffer, opdrachtenlijst

#print(ik_ben_vermoord(['jan', 'piet', 'korneel'],'piet'))

