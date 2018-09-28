# 1 sol in seconden
sol = (24 * 60 * 60) + (39 * 60) + 35.244

#Aardse tijdsaanduidingen (dagen, uren, minuten en seconden) in seconden
a = 24 * 60 * 60
b = 60 * 60
c = 60
d = 1

#invoer
aantal_marsdagen = int(input('Geef aantal marsdagen: '))

#tussenberekening sol in aantal Aardse tijdsaanduidingen (dagen, uren, minuten en seconden)
e = int((aantal_marsdagen * sol) // a)
f = int(((aantal_marsdagen * sol) - (e * a)) // b)
g = int(((aantal_marsdagen * sol) - (e * a) - (f * b)) // c)
h = int((aantal_marsdagen * sol) - (e * a) - (f * b) - (g * c) // d)


resultaat = str(aantal_marsdagen) + ' sol = ' + str(e) + ' dagen, ' + str(f) + ' uren, '
resultaat += str(g) + ' minuten en ' + str(h) + ' seconden'
print(resultaat)





