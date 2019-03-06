'''def woord_frequentie(tekst):
    dictionary = {}
    p_spatie = tekst.find(' ')
    p_punt = tekst.find('. ')
    grens = min(p_spatie, p_punt)
    woord = tekst[:grens].lower()
    tekst = tekst[grens + 1:]
    while p_punt != -1:
        if woord not in dictionary:
            dictionary[woord] = 1
        else:
            dictionary[woord] += 1
        p_spatie = tekst.find(' ')
        p_punt = tekst.find('. ')
        grens = min(p_spatie, p_punt)
        woord = tekst[:grens].lower()
        tekst = tekst[grens + 1:]
    return dictionary'''

def woord_frequentie(tekstje):
    dictionary = {}
    tekst = ''
    for teken in tekstje:
        if teken != '.' and teken != ',':
            tekst += teken
    tekst = tekst.split()
    for woord in tekst:
        woord = woord.lower()
        if woord in dictionary:
            dictionary[woord] += 1
        else:
            dictionary[woord] = 1
    return dictionary

#print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))

def woorden_per_frequentie(tekstje):
    dictionary = {}
    for key in woord_frequentie(tekstje):
        value = woord_frequentie(tekstje).get(key)
        if value in dictionary:
            dictionary[value].append(key)
        else:
            dictionary[value] = [key]
    return dictionary

#print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))

def meest_gebruikte_woorden(tekstje):
    return woorden_per_frequentie(tekstje).get(max(woorden_per_frequentie(tekstje)))

#print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))
