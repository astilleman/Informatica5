def germaniseer(zin):

    #alle letters overlopen
    for i in range(0, len(zin) - 1):

    # is het een spatie?
        if zin[i] == ' ':
        #ja -> volgende letter wordt een hoofdletter
            zin = zin[0: i + 1] + zin[i + 1].upper() + zin[i + 2:]
            #substring gaat nooit in fout, 1 letter wel

    return zin





print(germaniseer('Geluk helpt soms, moed altijd.'))