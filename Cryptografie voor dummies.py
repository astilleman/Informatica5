def versleutel_woord(woord, plaatsen):
    for i in range(len(woord)):
        if 97 <= ord(woord[i]) <= 122:
            woord = woord[:i] + woord[i].upper() + woord[i + 1:]
        ord_woord = ord(woord[i]) + plaatsen
        woord = woord[:i] + chr(ord_woord) + woord[i + 1:]
        if woord[i] == '@':
            woord = woord[:i] + ' ' + woord[i + 1:]
    return woord

#print(versleutel_woord('maar', 7))

def versleutel_zin(zin, plaatsen):
    p_spatie = zin.find(' ')
    zinnetje = versleutel_woord(zin[:p_spatie + 1], plaatsen)

    while p_spatie != -1:
        zin = zin[p_spatie + 1:]
        p_spatie = zin.find(' ')
        zinnetje += versleutel_woord(zin[:p_spatie + 1], plaatsen)
        zinnetje = zinnetje.replace(chr(32 + plaatsen), '@')

    zinnetje += versleutel_woord(zin[p_spatie + 1:], plaatsen)
    return zinnetje
#print(versleutel_zin('Persoonsgevens van maar liefst 143 miljoen Amerikanen werden er gehackt.', 12))

#############################################################"

'''def versleutel_woord(woord):
    verleuteld_woord = ''
    woord = woord.upper()
    for letter in woord:

        versleutelde_letter = chr(ord(letter) + n)

        if versleutelde_letter == '@':
            versleutelde_letter = ' '

        verleuteld_woord +=versleutelde_letter

    return verleuteld_woord

print(versleutel_woord('kaas', 1))

#####################################################

def versleutel_woord(woord, n):
    code = ''
    woord = woord.upper()
    for letter in woord:
        code_letter = chr(ord(letter) + n)

        if code_letter == '@':
            code_letter = ' '
        code += code_letter

    return code
#allemaal hoofdletters
#elke letter overlopen en getal bepalen + n
#nieuw getal terug letter
#@ spatie
#nieuw letter bij woord

def versleutel_zin(zin, getal):

    index_spatie = zin.find(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie + 1:]

        code += '@' + versleutel_woord(woord, getal)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, getal)

    return code'''
