from random import randint,seed
seed(1)
te_raden_getal = randint(1, 100)
gok = randint(1, 100)
eerste_getal = 1
tweede_getal = 100
pogingen = 0
mes = '[1,100] --> computer gokt {} \ '.format(gok)

while gok != te_raden_getal:
    pogingen += 1
    if tweede_getal - gok > gok - eerste_getal:
        tweede_getal -= gok
    else:
        eerste_getal += gok
    mes += '[{},{}] --> computer gokt {} \ '.format(eerste_getal, tweede_getal, gok)
    gok = randint(input((eerste_getal, tweede_getal))

#mes += 'computer had {} pogingen nodig om het getal {} te raden.'.format(pogingen, te_raden_getal)

#uitvoer
print(mes)