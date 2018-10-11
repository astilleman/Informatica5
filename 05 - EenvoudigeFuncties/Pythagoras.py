from math import sqrt

#invoer
a = float(input('Geef a: '))
b = float(input('Geef b: '))

#berekening c
c = sqrt((a ** 2) + (b ** 2))

#formattering op 2 cijfers na komma
a_op_honderdste = '{:.2f}'.format(a)
b_op_honderdste = '{:.2f}'.format(b)
c_op_honderdste = '{:.2f}'.format(c)

#uitvoer
resultaat = 'In een rechthoekige driehoek met rechthoekszijden a = ' + str(a_op_honderdste)
resultaat += ' en b = ' + str(b_op_honderdste) + ' is de schuine zijde ' + str(c_op_honderdste)
print(resultaat)

# formattering 1 regel en import bovenaan


