'''def behoort_tot_taal(tekst, set):
    nieuwe_lijst = []
    for letter in tekst:
        if letter != ' ':
            nieuwe_lijst.append(letter)
    nieuwe_set = set(nieuwe_lijst)


     return nieuwe_lijst

print(behoort_tot_taal('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))'''

def behoort_tot_taal(tekst, letters):
    nieuwe_set = set(tekst)
    nieuwe_set.discard(' ')
    if nieuwe_set.issubset(letters) is True and len(nieuwe_set) > 0:
        mes = True
    else:
        mes = False
    return mes

#print(behoort_tot_taal('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))

def is_onleesbaar(tekst, letters):
    nieuwe_set = set(tekst)
    nieuwe_set.discard(' ')
    return nieuwe_set.isdisjoint(letters)

#print(is_onleesbaar('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))

def perfect_woord(tekst, letters):
    nieuwe_set = set(tekst)
    nieuwe_set.discard(' ')
    return nieuwe_set == letters

#print(perfect_woord('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))







