getal = int(input('Geef een geheel getal: '))
n = 2
nieuw_getal = 0

while getal % n != 0:
    nieuw_getal = getal % n
    n += 1

if getal == 1 or nieuw_getal != 0:
    print('priemgetal')

else:
    print('geen priemgetal')

