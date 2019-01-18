'''def tel_woorden_dov(zin):
    return len(zin) - len(zin.replace(' ', '')) + 1

#altijd 1 woord meer dan

def tel_woorden(zin):

    aantal_spaties = 1

    for letter in zin:
        if letter == ' ':
            aantal_spaties += 1

    return aantal_spaties #klas'''

def tel_woorden(zin):

    aantal_woorden = 1

    for i in range(len(zin)):

         if zin[i] == ' ':
            aantal_woorden += 1

    return aantal_woorden

#print(tel_woorden('Die.'))

def langste_zin(tekst):

    p_punt = tekst.find('.')
    zin = tekst[:p_punt + 1]
    lengte_langste_zin = len(zin)
    langste_zin = zin


    while p_punt != -1:
        tekst = tekst[p_punt + 2:]
        p_punt = tekst.find('.')
        zin = tekst[:p_punt + 1]

        if len(zin) > lengte_langste_zin:
            lengte_langste_zin = len(zin)
            langste_zin = zin

        p_punt = tekst.find('.')

    aantal_woorden_langste_zin = tel_woorden(langste_zin)

    return aantal_woorden_langste_zin

#print
print(langste_zin('De kaaimantaks zou de financiële sluiproutes naar belastingsparadijzen droogleggen. Veel woorden maar weinig daden, lijkt me, afgaand op wat hier is gezegd. Kortom, de belastingparadijzen en het einde van de belastingparadijzen zijn niet aan de orde. Tenzij de regering alsnog orde op zaken stelt. Maar in lopende zaken is dat niet vanzelfsprekend.'))

