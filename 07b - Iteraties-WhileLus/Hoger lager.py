from random import randint,seed
seed(1)
te_raden_getal = randint(1, 100)
eerste_getal = 1
tweede_getal = 100
gok = randint(eerste_getal, tweede_getal)
pogingen = 1
mes = '[1,100] --> computer gokt {}\n'.format(gok)

while gok != te_raden_getal:
    pogingen += 1
    if tweede_getal - gok > gok - eerste_getal:
        eerste_getal += gok
    else:
        tweede_getal = gok - 1
    gok = randint(eerste_getal, tweede_getal)
    mes += '[{},{}] --> computer gokt {}\n'.format(eerste_getal, tweede_getal, gok)
    seed(1)

mes += 'computer had {} pogingen nodig om het getal {} te raden.'.format(pogingen, te_raden_getal)

#uitvoer
print(mes)