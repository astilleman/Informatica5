def fruitmand_maken(fruitlijst):
    fruitdictionary = {}
    for fruit in fruitlijst:
        fruitdictionary[len(fruit)] = fruit
    return fruitdictionary

#print(fruitmand_maken(['banaan', 'aardbei', 'kiwi', 'peer', 'appel', 'bes', 'sinaasappel', 'framboos']))
#print(fruitmand_maken(['aardbei']))

def fruitmand_inpakken(fruitdicitionary):
    fruitlijst = []
    for i in range(max(fruitdicitionary) + 1):
        if i in fruitdicitionary:
            fruitlijst.append(fruitdicitionary.get(i))
    return fruitlijst

#print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))
#print(fruitmand_inpakken({7: 'aardbei'}))