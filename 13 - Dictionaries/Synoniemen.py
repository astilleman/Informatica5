def synoniemen(zin, synoniemen):

    zin = zin.split()

    # zoek elk woord in de lijst op in het synoniemenwoordenboek
    for i in range(len(zin)):
        if zin[i] in synoniemen:
            zin[i] = synoniemen.get(zin[i])

    # indien ...

    # anders ... niets doen is niets programmeren

    zin = ' '.join(zin)

    return zin


#print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))