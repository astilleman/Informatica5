#invoer
kleur_h1 = input('Geef kleur hoed 1: ')
kleur_h_2 = input('Geef kleur hoed 2: ')
persoon_omgekeerde_kleur = int(input('Geef persoon met omgekeerde hoed: '))

#berekening
if kleur_h1 == 'zwart' and kleur_h_2 == 'zwart' and persoon_omgekeerde_kleur == 1:
    print('wit')
    print('zwart')
elif kleur_h1 == 'zwart' and kleur_h_2 == 'zwart' and persoon_omgekeerde_kleur == 2:
    print('zwart')
    print('wit')
elif kleur_h1 == 'wit' and kleur_h_2 == 'wit' and persoon_omgekeerde_kleur == 1:
    print('zwart')
    print('wit')
elif kleur_h1 == 'wit' and kleur_h_2 == 'wit' and persoon_omgekeerde_kleur == 2:
    print('wit')
    print('zwart')
elif kleur_h1 == 'zwart' and kleur_h_2 == 'wit' and persoon_omgekeerde_kleur == 1:
    print('zwart')
    print('zwart')
elif kleur_h1 == 'zwart' and kleur_h_2 == 'wit' and persoon_omgekeerde_kleur == 2:
    print('wit')
    print('wit')
elif kleur_h1 == 'wit' and kleur_h_2 == 'zwart' and persoon_omgekeerde_kleur == 1:
    print('wit')
    print('wit')
elif kleur_h1 == 'wit' and kleur_h_2 == 'zwart' and persoon_omgekeerde_kleur == 2:
    print('zwart')
    print('zwart')