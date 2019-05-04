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

'''
zelffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fruit = input('Geef een fruit: ')

fruitmand = {'kiwi': 3, 'bes': 12, 'peer': 5}

aantal = fruitmand.get(fruit)

if aantal is None:
    mes = 'Ik had graag ' + str(sum(fruitmand.values())) + ' stukken ' + fruit + ' besteld.'

else:
    mes = 'Ik had graag ' + str(2 * aantal) + ' stukken ' + fruit + ' bijbesteld.'

print(mes)'''