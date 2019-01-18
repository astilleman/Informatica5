def positie_laagste_ascii(tekst):

    p_laagste = 0
    ord_laagste = ord(tekst[0])

    for i in range(1, len(tekst)):

        ord_huidige = ord(tekst[i])

        if ord_huidige < ord_laagste:
            p_laagste = i
            ord_laagste = ord_huidige

    return p_laagste

print(positie_laagste_ascii('vincent.vangogh@gmail.com'))

def sorteer(tekst):
    s_tekst = ''

    while len(tekst) > 0:
        i = positie_laagste_ascii(tekst)
        s_tekst += tekst[i]
        tekst = tekst[:i] + tekst[i + 1:]

    return s_tekst

print(sorteer('vincent.vangogh@gmail.com'))

def is_alfabetisch(tekst):
    return tekst == sorteer(tekst)

print(is_alfabetisch('beknopt'))

