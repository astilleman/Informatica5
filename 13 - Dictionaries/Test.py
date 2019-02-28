fruitmand = {}

fruitstuk = input('fruitstuk: ')

while fruitstuk != 'stop':
    aantal = int(input('aantal: '))

    if fruitstuk in fruitmand:
        fruitmand[fruitstuk] += aantal
    else:
        fruitmand[fruitstuk] = aantal

    print(fruitmand)

    fruitstuk = input('fruitstuk: ')
