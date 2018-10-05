#invoer
luchttemperatuur_t = float(input('Geef lucttemperatuur: '))
windsnelheid_w = float(input('Geef windsnelheid: ')) * (1 / 3.6)

#uitvoer
uitvoer = 13.12 + (0.6215 * luchttemperatuur_t)
uitvoer += ((0.3965 * luchttemperatuur_t) - 11.37) * pow(3.6 * windsnelheid_w, 0.16)
print(uitvoer)