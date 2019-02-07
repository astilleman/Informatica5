def versleuteld_woord(woord, n):

    nieuw_woord = ''

    woord = woord.upper()

    for letter in woord:
        nieuw_woord += chr(ord(letter) + n)

    for i in range(len(nieuw_woord)):
        if nieuw_woord[i] == '@':
            nieuw_woord = nieuw_woord[:i] + ' ' + nieuw_woord[i + 1:]

    return nieuw_woord

print(versleuteld_woord('maar', 7))

def versleutel_zin(zin, n):
    versleuteld = ''
    positie_spatie = zin.find(' ')
    woord = zin[:positie_spatie]

    while positie_spatie != -1:
        versleuteld += versleuteld_woord(woord, n) + '@'
        zin = zin[positie_spatie + 1:]
        positie_spatie = zin.find(' ')
        woord = zin[:positie_spatie]

    versleuteld += versleuteld_woord(zin, n)

    return versleuteld


print(versleutel_zin('Persoonsgegevens van maar liefst 143 miljoen Amerikanen werden er gehackt.', 12))





