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






