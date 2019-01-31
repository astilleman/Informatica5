def ontdubbelen(woord):
    for i in range(len(woord) - 1):
        if woord[i] == woord[i + 1]:
            woord = woord[:i] + ' ' + woord[i + 1:]
    woord = woord.replace(' ', '')

    return woord

print(ontdubbelen('aaien'))

##################################################################################

def ontdubbelen(woord):

    nieuw_woord = woord[0]

    for i in range(0, len(woord)):

        if woord[i] != woord[i - 1]:
            nieuw_woord += woord[i]

    return nieuw_woord

print(ontdubbelen('groooottee'))