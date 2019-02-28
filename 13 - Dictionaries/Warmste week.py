def gift_inschrijven(klas_bedrag, giften):

    if klas_bedrag[0] in giften:
        giften[klas_bedrag[0]] += klas_bedrag[1]

    else:
        giften[klas_bedrag[0]] = klas_bedrag[1]

    return giften

print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))
print(gift_inschrijven(('5WWI', 71.47),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 161.01}))
print(gift_inschrijven(('5IN', 73.81),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))