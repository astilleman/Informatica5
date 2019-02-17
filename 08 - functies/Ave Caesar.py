def is_letter(n):
    if 65 <= ord(n) <= 90 or 97 <= ord(n) <= 122:
        uitspraak = True
    else:
        uitspraak = False
    return uitspraak

def roteer_letter(n, x):
    positie = ord(n) + x
    nieuwe_letter = None
    if 65 <= ord(n) <= 90:
        if positie > 90:
            positie -= 26
        nieuwe_letter = chr(positie)
    elif 97 <= ord(n) <= 122:
        if positie > 122:
            positie -= 26
        nieuwe_letter = chr(positie)
    return nieuwe_letter

def versleutel(y, x):
    boodschap = ''
    for i in y:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            i = roteer_letter(i, x)
        else:
            i = i
        boodschap += i
    return boodschap

#'Dmzbzwce wx rm szikpb mv dqmz pmb tmdmv!'
#'Byn fypyh vymnuun piil 10% ocn xchayh xcy ayvyolyh yh piil 90% ocn biy dcd xuulij lyuayyln.'
#toets !!! versleutel en roteer!!!
