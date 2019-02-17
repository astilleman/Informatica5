def graad(woord):
    message, graad = '', 0
    for i in range(1, len(woord)):
        if woord[0] == woord[i] and woord[i:] == woord[:len(woord) - i] and len(woord) - i > graad:
            message = True
            graad = len(woord) - i
    if message is not True:
        message = False
    if message is False:
        waarde = 0
    else:
        waarde = graad
    return waarde

#print(graad('oliaoli'))

def slinger(woord, r):
    if graad(woord) == 0:
        herhaling = r * woord
    elif r == 0:
        herhaling = ''
    else:
        herhaling = woord + (r - 1) * woord[graad(woord):]
    return herhaling

#print(slinger('khuskhus', 0))

###########################################################################################"
def graad(woord):
    p_2de_woord = woord.find(woord[0], 1)
    lengte_woord = len(woord[p_2de_woord:])
    if woord[:lengte_woord] == woord[p_2de_woord:]:
        graad = lengte_woord
    else:
        graad = 0

    return graad

#print(graad('alfalfa'))

def slinger(woord, r):
    if graad(woord) == 0:
        slingerwoord = r * woord
    else:
        slingerwoord = r * woord[:len(woord) - graad(woord)] + woord[len(woord) - graad(woord):]

    return slingerwoord

#print(slinger('onion', 7))






