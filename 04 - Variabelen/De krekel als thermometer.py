#invoer
aantal_tsjirps_per_minuut = int(input('Geef aantal tsjirps per minuut: '))

#berekening
temperatuur_in_fahrenheit = 50 + ((aantal_tsjirps_per_minuut - 40) / 4)
temperatuur_in_celsius = 10 + ((aantal_tsjirps_per_minuut - 40) / 7)

resultaat_fahrenheit = 'temperatuur (Fahrenheit): ' + str(temperatuur_in_fahrenheit)
resultaat_celsius = 'temperatuur (Celsius): ' + str(temperatuur_in_celsius)
print(resultaat_fahrenheit)
print(resultaat_celsius)

