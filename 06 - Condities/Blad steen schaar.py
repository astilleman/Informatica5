#invoer
speler_1 = input('Antwoord speler 1: ')
speler_2 = input('Antwoord speler 2: ')

#berekening
if speler_1 == 'blad' and speler_2 == 'steen':
    print('speler_1 wint')
elif speler_1 == 'blad'and speler_2 == 'schaar':
    print('speler 2 wint')
elif speler_1 == 'steen' and speler_2 == 'schaar':
    print('speler 1 wint')
elif speler_1 == 'steen' and speler_2 == 'blad':
    print('speler 2 wint')
elif speler_1 == 'schaar' and speler_2 == 'blad':
    print('speler 1 wint')
elif speler_1 == 'schaar' and speler_2 == 'steen':
    print('speler 2 wint')
else:
    print('onbeslist')
