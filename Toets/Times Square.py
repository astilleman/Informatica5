def bereken_prijs(gecodeerde_boodschap):
    p_kleiner_dan_bekje = gecodeerde_boodschap.find('<')
    p_groter_dan_bekje = gecodeerde_boodschap.find('>')
    boodschap = gecodeerde_boodschap[:p_kleiner_dan_bekje]
    prijs_per_letter = float(gecodeerde_boodschap[p_kleiner_dan_bekje + 1:p_groter_dan_bekje])
    prijs = len(boodschap) * prijs_per_letter
    return boodschap, prijs

#print(bereken_prijs('I spent my last money on this billboard. Please give me a job.<2.68>'))

def toon_boodschappen(gecodeerde_boodschappen):

    p_groter_dan_bekje = gecodeerde_boodschappen.find('>')
    totale_prijs, boodschappen = 0, ''

    while p_groter_dan_bekje != -1:
        boodschap = gecodeerde_boodschappen[:p_groter_dan_bekje + 1]
        boodschapje ,prijs = bereken_prijs(boodschap)
        totale_prijs += prijs
        boodschappen += '\n' + boodschapje
        gecodeerde_boodschappen = gecodeerde_boodschappen[p_groter_dan_bekje + 1:]
        p_groter_dan_bekje = gecodeerde_boodschappen.find('>')
        message = str(totale_prijs) + boodschappen


    return message

#print(toon_boodschappen('I spent my last money on this billboard. Please give me a job.<2.68>Dear Emma, I love You more than words can say. Please wil you marry me?<2.42>I LOVE YOU AND WANT TO SPENT FOREVER WITH YOU. WILL YOU MARRY ME?<0.76>'))


