def positie_laagste_ascii(tekst):
    positie, ascii_waarde = 128, 128
    for i in range(0, len(tekst)):
        if ord(tekst[i]) < ascii_waarde:
            positie = i
            ascii_waarde = ord(tekst[i])
    return positie

#print(positie_laagste_ascii('vincent.vangogh@gmail.com'))

def sorteer(tekst):
    gesorteerd = tekst[positie_laagste_ascii(tekst)]
    for i in range(1, len(tekst)):
        tekst = tekst[:positie_laagste_ascii(tekst)] + tekst[positie_laagste_ascii(tekst) + 1:]
        gesorteerd += tekst[positie_laagste_ascii(tekst)]
    return gesorteerd

#print(sorteer('LEGO'))

def is_alfabetisch(tekst):
    if tekst == sorteer(tekst):
        message = True
    else:
        message = False
    return message

#print(is_alfabetisch('beknopt'))