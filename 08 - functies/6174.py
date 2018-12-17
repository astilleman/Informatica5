def splits(a):
    c1 = a // 1000
    c2 = (a - (c1 * 1000)) // 100
    c3 = (a - (c1 * 1000) - (c2 * 100)) // 10
    c4 = a - (c1 * 1000) - (c2 * 100) - (c3 * 10)
    return c1, c2, c3, c4

def oplopende_cijfers(b, c, d, e):
    getal1 = min(b, c, d, e)
    getal2 = max(min(b, c, d), min(b, c, e), min(b, d, e), min(c, d, e))
    getal3 = min(max(b, c, d), max(b, c, e), max(b, d, e), max(c, d, e))
    getal4 = max(b, c, d, e)
    return getal1, getal2, getal3, getal4

def op_af_getallen(f, g, h, i):
    op_rij, af_rij = '', ''
    op_rij += str(f)+ str(g) + str(h) + str(i)
    af_rij += str(i)+ str(h) + str(g) + str(f)
    return op_rij, af_rij

def verschil(j, k):
    verschil = str(int(j) - int(k))
    return verschil

def kaprekar(a):
    uitkomst = ''
    c1 = a // 1000
    c2 = (a - (c1 * 1000)) // 100
    c3 = (a - (c1 * 1000) - (c2 * 100)) // 10
    c4 = a - (c1 * 1000) - (c2 * 100) - (c3 * 10)
    getal1 = min(c1, c2, c3, c4)
    getal2 = max(min(c1, c2, c3), min(c1, c2, c4), min(c1, c3, c4), min(c2, c3, c4))
    getal3 = min(max(c1, c2, c3), max(c1, c2, c4), max(c1, c3, c4), max(c2, c3, c4))
    getal4 = max(c1, c2, c3, c4)
    op_rij = str(getal1) + str(getal2) + str(getal3) + str(getal4)
    af_rij = str(getal4) + str(getal3) + str(getal2) + str(getal1)
    if verschil(af_rij, op_rij) == '6174':
        uitkomst += '{} - {} = {}'.format(af_rij, op_rij, 6174)
    else:
        while verschil(af_rij, op_rij) != '6174':
            uitkomst += '{} - {} = {}\n'.format(af_rij, op_rij, verschil(af_rij, op_rij))
            b = int(verschil(af_rij, op_rij))
            c1 = b // 1000
            c2 = (b - (c1 * 1000)) // 100
            c3 = (b - (c1 * 1000) - (c2 * 100)) // 10
            c4 = b - (c1 * 1000) - (c2 * 100) - (c3 * 10)
            getal1 = min(c1, c2, c3, c4)
            getal2 = max(min(c1, c2, c3), min(c1, c2, c4), min(c1, c3, c4), min(c2, c3, c4))
            getal3 = min(max(c1, c2, c3), max(c1, c2, c4), max(c1, c3, c4), max(c2, c3, c4))
            getal4 = max(c1, c2, c3, c4)
            op_rij = str(getal1) + str(getal2) + str(getal3) + str(getal4)
            af_rij = str(getal4) + str(getal3) + str(getal2) + str(getal1)
        c1 = b // 1000
        c2 = (b - (c1 * 1000)) // 100
        c3 = (b - (c1 * 1000) - (c2 * 100)) // 10
        c4 = b - (c1 * 1000) - (c2 * 100) - (c3 * 10)
        getal1 = min(c1, c2, c3, c4)
        getal2 = max(min(c1, c2, c3), min(c1, c2, c4), min(c1, c3, c4), min(c2, c3, c4))
        getal3 = min(max(c1, c2, c3), max(c1, c2, c4), max(c1, c3, c4), max(c2, c3, c4))
        getal4 = max(c1, c2, c3, c4)
        op_rij = str(getal1) + str(getal2) + str(getal3) + str(getal4)
        af_rij = str(getal4) + str(getal3) + str(getal2) + str(getal1)
        uitkomst += '{} - {} = {}'.format(af_rij, op_rij, 6174)
    return uitkomst











