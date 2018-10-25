#invoer
s1 = input('speler 1: ')
s2 = input('speler 2: ')

#rekenwerk

if s1 == s2:
    mes = 'onbeslist'

#speler 1 wint
elif (s1 == 'blad' and s2 == 'steen') or (s1 == 'steen' and s2 == 'schaar') or (s1 == 'schaar' and s2 == 'blad'):

#speler 2 wint
else:
    mes = 'speler 2 wint'


#uitvoer
print(mes)


#makkelijkste in if en moeilijkste in else