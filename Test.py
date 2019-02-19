def fruitstuk_toevoegen(fruitmand, fruitstuk):
    mes = 'zelfde fruit'
    if fruitstuk not in fruitmand:
        mes = True
    i = 0
    while i < len(fruitmand) and mes is True:
        if len(fruitmand[i]) == len(fruitstuk):
            mes = False
        i += 1
    if mes is True:
        fruitmand.append(fruitstuk)
        fruitmand.sort(key=len)
    elif mes is False:
        fruitmand[i - 1:i] = []
        fruitmand.insert(i - 1,fruitstuk)
    return fruitmand

print(fruitstuk_toevoegen(['kiwi'],'peer'))
print(fruitstuk_toevoegen(['kiwi'],'kiwi'))
print(fruitstuk_toevoegen(['bes', 'peer', 'framboos', 'sinaasappel'],'appel'))

def maak_fruitmand(lijst):
    fruitmand = []
    for fruit in lijst:
        fruitstuk_toevoegen(fruitmand, fruit)
    return fruitmand

print(maak_fruitmand(['kiwi', 'peer', 'kiwi', 'peer', 'kiwi']))
print(maak_fruitmand(['bes', 'appel', 'framboos']))
