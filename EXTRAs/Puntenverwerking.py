'''Opgave
Schrijf een functie eindcijfer die voor elke student het eindcijfer als volgt berekent:

Theorie: 25%
Recursie: 25%
Oefeningen: 50%
Als een cijfer voor één van de onderdelen ontbreekt, dan wordt een nulscore toegekend.
Het eindcijfer is een geheel getal op twintig, wiskundig afgerond (gebruik de functie round).

De functie retourneert een dictionary met als sleutel de naam van de student en als waarde het behaalde eindcijfer (int).

Schrijf een functie groepeer die de studenten groepeert volgens hun cijfer.
De functie heeft als argument een dictionary met punten voor de verschillende onderdelen zoals hierboven beschreven
en retourneert een dictionary met als sleutels de behaalde cijfers en als waarden een set met de namen van de studenten (strings) die dit cijfer behaalden.'''



def eindcijfer(puntendictionary):
    einddictionary = {}
    resultaat = 0
    for leerling, leerlingresultaat in puntendictionary.items():
        for onderdeel in leerlingresultaat:
            if onderdeel == "Theorie":
                resultaat += 0.25 * (leerlingresultaat.get(onderdeel)/20)
            elif onderdeel == "Recursie":
                resultaat += 0.25 * (leerlingresultaat.get(onderdeel)/20)
            elif onderdeel == "Oefeningen":
                resultaat += 0.5 * (leerlingresultaat.get(onderdeel)/20)
        resultaat *= 20
        einddictionary[leerling] = round(resultaat)
        resultaat = 0
    return einddictionary

'''print(eindcijfer({
    "Berry Westra": { "Theorie": 12, "Recursie": 14, "Oefeningen": 18},
    "Mike Lawrence": { "Theorie": 8, "Recursie": 6, "Oefeningen": 9},
    "Victor Mollo": { "Theorie": 12, "Recursie": 4, "Oefeningen": 14},
    "Michel Lebel": { "Theorie": 18},
    "Terence Reece": { "Recursie": 4, "Oefeningen": 14}}))'''

def ongesorteerd(puntendictionary):
    einddictionary = {}
    leerlingresultaat = eindcijfer(puntendictionary)
    for leerling, resultaat in leerlingresultaat.items():
        if resultaat in einddictionary:
            einddictionary[resultaat].add(leerling)
        else:
            einddictionary[resultaat] = {leerling}
    return einddictionary

def groepeer(puntendictionary):
    puntendictionary = ongesorteerd(puntendictionary)
    einddictionary = {}
    for i in range(1, max(puntendictionary) + 1):
        if i in puntendictionary:
            einddictionary[i] = puntendictionary.get(i)
    return einddictionary


print(groepeer({
    "Berry Westra": { "Theorie": 12, "Recursie": 14, "Oefeningen": 18},
    "Mike Lawrence": { "Theorie": 8, "Recursie": 6, "Oefeningen": 9},
    "Victor Mollo": { "Theorie": 12, "Recursie": 4, "Oefeningen": 14},
    "Michel Lebel": { "Theorie": 18},
    "Terence Reece": { "Recursie": 4, "Oefeningen": 14}}))
