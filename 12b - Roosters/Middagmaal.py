'''middagmaal = 5.3
soep = 1.7
vieruurtje = 2.3'''
def maaltijdprijs(maaltijdtype, aantal):

    maaltijdprijs = 0

    if maaltijdtype == 'middagmaal':
        maaltijdprijs = aantal * 5.3
    elif maaltijdtype == 'soep':
        maaltijdprijs = aantal * 1.7
    elif maaltijdtype == 'vieruurtje':
        maaltijdprijs = aantal * 2.3

    return maaltijdprijs

def dagprijs(bestelling):

    dagprijs = 0

    #overloop de bestelling in stapjes van 2
    for i in range(0, len(bestelling), 2):
        dagprijs += maaltijdprijs(bestelling[i], bestelling[i + 1])

    return dagprijs

#print(dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2)))
#print(dagprijs(('middagmaal', 2, 'vieruurtje', 2)))

def weekprijs(bestelling):

    weekprijs = 0

    for dag in bestelling:

        weekprijs += dagprijs(dag)

    return weekprijs

#print(weekprijs((('middagmaal', 2, 'soep', 2, 'vieruurtje', 2), ('middagmaal', 1, 'soep', 1), ('soep', 3, 'vieruurtje', 3), ('middagmaal', 3, 'soep', 1), ('middagmaal', 3, 'soep', 3, 'vieruurtje', 1))))