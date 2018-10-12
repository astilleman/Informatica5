#invoer
temperatuur = float(input('Geef de temperatuur in Kelvin: '))
lichtkracht = float(input('Geef de lichtkracht t.o.v. de zon: '))

#berekening
if lichtkracht > 10000:
    print('superreuzen (a)')
elif lichtkracht > 1000:
    print('superreuzen (b)')
elif temperatuur < 7500 and lichtkracht > 100:
    print('heldere reuzen')
elif temperatuur < 6000 and lichtkracht > 10:
    print('reuzen')
elif (3000 < temperatuur < 5000 and lichtkracht < 0.0001) or (temperatuur > 5000 and lichtkracht < 0.01):
    print('witte dwergen')
else:
    print('hoofdreeks')