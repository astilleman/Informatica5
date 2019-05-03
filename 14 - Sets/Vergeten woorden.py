def vergeten_woorden(tekst, verplicht):
    verzameling = set(tekst.split())

    #verplichte woorden
    aantal_verplicht = len(verplicht)

    #vergeten woorden
    aantal_vergeten = len(verplicht.difference(verzameling))

    #gebruikte woorden
    aantal_gebruikt = aantal_verplicht - aantal_vergeten
    # of len(verplicht.intersection(verzameling))

    return aantal_verplicht, aantal_vergeten, aantal_gebruikt

print(vergeten_woorden('',{'python', 'world', 'hello', 'java'}))