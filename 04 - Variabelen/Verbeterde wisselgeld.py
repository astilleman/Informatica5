#input
bedrag = int(input('Geef een bedrag in eurocenten: '))

#berekening
stukken_1_euro = bedrag // 100
rest = bedrag % 100
stukken_50_cent = rest // 50
rest %= 50
stukken_20_cent = rest // 20
rest %= 20
stukken_10_cent = rest // 10
rest %= 10
stukken_5_cent = rest // 5
rest %= 5
stukken_2_cent = rest // 2
rest %= 2
stukken_1_cent = rest

aantal_stukken = stukken_1_euro + stukken_50_cent + stukken_20_cent + stukken_10_cent
aantal_stukken += stukken_5_cent + stukken_2_cent + stukken_1_cent

#print
print(bedrag, 'cent kan je omwisselen in', aantal_stukken, 'munstukken')