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


####################################################################################"
'''def woord_frequentie(tekst):

    tekst = tekst.lower()
    tekst = tekst.replace('.', ' ')
    tekst = tekst.replace(',', ' ')
    tekst = tekst.split()

    dictionary = {}

    for woord in tekst:

        if woord in dictionary:
            dictionary[woord] += 1

        else:
            dictionary[woord] = 1

    return dictionary
    
def woorden_per_frequentie(tekst):

    dictionary = {}

    for woord in woord_frequentie(tekst):
        if woord_frequentie(tekst).get(woord) in dictionary:
            dictionary[woord_frequentie(tekst).get(woord)].append(woord)
        else:
            dictionary[woord_frequentie(tekst).get(woord)] = [woord]

    return dictionary
    
#################laatste versie

def woord_frequentie(tekst):
    freq_dict = {}
    tekst = tekst.replace('.', '')
    tekst = tekst.replace(',', '')
    tekst = tekst.lower()
    tekst = tekst.split()
    for woord in tekst:
        if woord in freq_dict:
            freq_dict[woord] += 1
        else:
            freq_dict[woord] = 1
    return freq_dict

#print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))

def woorden_per_frequentie(tekst):
    freq_dict = {}
    for key, value in woord_frequentie(tekst).items():
        if value in freq_dict:
            freq_dict[value].append(key)
        else:
            freq_dict[value] = [key]
    return freq_dict

#print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))

def meest_gebruikte_woorden(tekst):
    return woorden_per_frequentie(tekst).get(max(woorden_per_frequentie(tekst)))

#print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))
    
    '''

