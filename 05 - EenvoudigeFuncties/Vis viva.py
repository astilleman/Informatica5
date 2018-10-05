#gegevens
geocentrische_gravitatieconstante = 398600.4418 * pow(10, 9)

#invoer
r = float(input('Geef afstand tussen satelliet en middelpunt Aarde: '))
v = float(input('Geef snelheid satelliet t.o.v. Aarde: '))

#berekening grote as
a = (geocentrische_gravitatieconstante) * r
a /= (2 * geocentrische_gravitatieconstante) - (r * (v ** 2))

#berekening periode in seconden
from math import pi, sqrt
p_in_seconden = 2 * pi * sqrt((a ** 3) / geocentrische_gravitatieconstante)

#berekening periode in dagen, uren en minuten
d = int(p_in_seconden // 86400)
u = int((p_in_seconden % 86400) // 3600)
m = int(((p_in_seconden % 86400) % 3600) // 60)

#uitvoer
uitvoer_a = 'grote as: ' + str(a) + ' meter'
uitvoer_p_in_seconden = 'periode: ' + str(p_in_seconden) + ' seconden'
uitvoer_p = 'periode: ' + str(d) + ' dagen, '
uitvoer_p += str(u) + ' uren en ' + str(m) + ' minuten'

print(uitvoer_a)
print(uitvoer_p_in_seconden)
print(uitvoer_p)
