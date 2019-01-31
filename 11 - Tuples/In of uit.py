from math import sqrt


def binnen_of_buiten(m, c, p):
    #straal = d(m, c)
    # d(m, p) -> d_mp
    #print(r, d_mp)
    # if r == dmp:
    #elif
    #else
    # 1 keer pow
    straal = sqrt(pow((c[0] - m[0]), 2) + pow((c[1] - m[1]), 2))
    afstand = sqrt(pow((p[0] - m[0]), 2) + pow((p[1] - m[1]), 2))

    if afstand == straal:
        message = 'op'
    elif afstand >  straal:
        message = 'buiten'
    else:
        message = 'binnen'

    return message, round(afstand, 4)

print(binnen_of_buiten((7, -1),(-9, -32),(12, -48)))


