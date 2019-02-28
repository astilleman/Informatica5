def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):

    if ploeg in inschrijvingen and len(inschrijvingen[ploeg]) > 1:
        inschrijvingen[ploeg].remove(deelnemer)

    else:
        inschrijvingen.pop(ploeg)

    return inschrijvingen

#print(verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
#print(verlaat_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))

def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):

    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(deelnemer)

    else:
        inschrijvingen[ploeg] = [deelnemer]


    return inschrijvingen

#print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
#print(vervoegt_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))

