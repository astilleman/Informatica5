'''OPGAVE
Schrijf een functie groep waaraan een reeks (een lijst of een tuple) van strings moet doorgegeven worden die een groep stenen voorstelt.
De functie moet een dictionary teruggeven die de gegeven groep stenen voorstelt.

Schrijf een functie uitleggen waaraan twee dictionaries moeten doorgegeven worden. De eerste stelt een rijtje stenen voor die een speler wil uitleggen.
De tweede stelt de stenen voor die de speler op zijn rekje heeft staan.
De functie moet een Booleaanse waarde teruggeven die aangeeft of de speler het gegeven rijtje stenen kan uitleggen.
Dat is het geval als alle stenen van het rijtje wel degelijk op het gegeven rekje staan, rekening houdend met het aantal keer dat de stenen voorkomen in het rijtje en op het rekje.
Indien de speler het gegeven rijtje kan uitleggen, dan moet de functie er ook voor zorgen dat die stenen weggehaald worden uit de dictionary die de stenen op het rekje voorstelt.
Indien de speler het gegeven rijtje niet kan uitleggen, dan mag de functie de gegeven dictionary die de stenen op het rekje voorstelt niet wijzigen.'''


def groep(stenen):
    stenen_dictionary = {}
    for steen in stenen:
        if steen in stenen_dictionary:
            stenen_dictionary[steen] += 1
        else:
            stenen_dictionary[steen] = 1
    return stenen_dictionary

#print(groep(['1G', '7G', '8G', '12G', '12B', '13B', '13B', '13Z', '13G', '2Z', '3Z', '4Z', '11Z', '11Z', '4R', '5R']))
#print(groep(['9G', '7R', '9G', '7R', '9G', '7R', '9G']))

def uitleggen(uitleggen, rekje):
    if set(uitleggen).issubset(set(rekje)):
        i = 0
        mes = True
        while i < len(uitleggen) and mes is True:
            if groep(uitleggen).get(uitleggen[i]) <= groep(rekje).get(uitleggen[i]):
                rekje.remove(uitleggen[i])
                i += 1
            else:
                mes = False
    else:
        mes = False
    return mes, rekje

#print(uitleggen(['13B', '13Z', '13G'],['1G', '7G', '8G', '12G', '12B', '13B', '13B', '13Z', '13G', '2Z', '3Z', '4Z', '11Z', '11Z', '4R', '5R']))
#print(uitleggen(['12B', '12Z', '12G'],['1G', '7G', '8G', '12G', '12B', '13B', '13B', '13Z', '13G', '2Z', '3Z', '4Z', '11Z', '11Z', '4R', '5R']))