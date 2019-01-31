def geldige_zet(zet):

    message = False

    if zet[0] in 'KDTLP' and zet[1] in 'abcdefgh' and 49 <= ord(zet[2]) <= 56 and len(zet) == 3:
        message = True

    elif zet[0] in 'abcdefgh' and 49 <= ord(zet[1]) <= 56 and len(zet) == 2:
        message = True

    return message

#print(geldige_zet('DB36'))

def geldige_zetten(reeks):

    i = 0
    boodschap = True

    while boodschap != False and i != len(reeks):

        if geldige_zet(reeks[i]) == True:
            i += 1

        else:
            boodschap = False

    if i == len(reeks):
        boodschap = True

    else:
        boodschap = False

    return boodschap

#print(geldige_zetten(('Ta1', 'e5', 'h8', 'f7', 'Db7', 'Lg3')))



