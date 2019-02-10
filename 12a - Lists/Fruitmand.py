def fruitstuk_toevoegen(fruitmand, fruitstuk):

    mes = 'zelfde fruit'

    if fruitstuk not in fruitmand:
        mes = True

    i = 0

    for fruit in fruitmand:

        while mes is True and i < len(fruitmand):

            if len(fruit) == len(fruitstuk):
                mes = False

            i += 1

    if mes is True:
        fruitmand.append(fruitstuk)
        fruitmand.sort(key=len)

    elif mes is False:
        fruitmand[i-1:i] = []
        fruitmand.insert(i - 1, fruitstuk)

    return fruitmand


#print(fruitstuk_toevoegen(['kiwi'],'peer'))

def maak_fruitmand(fruitlijst):

    fruitmand = []

    for fruit in fruitlijst:
        fruitmand = fruitstuk_toevoegen(fruitmand, fruit)

    return fruitmand

#print(maak_fruitmand(['aardbei', 'peer', 'bes']))




