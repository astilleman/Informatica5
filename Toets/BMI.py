#invoer
gelijke_lengte = float(input('Geef de gelijke lengte van persoon 1 en 2: '))
naam1= str(input('Geef de naam van persoon 1: '))
gewicht1 = float(input('Geef het gewicht van persoon 1: '))
naam2 = str(input('Geef de naam van persoon 2: '))
gewicht2 = float(input('Geef het gewicht van persoon 2: '))

#berekening
bmi = (max(gewicht1, gewicht2)) / (gelijke_lengte ** 2)

if gewicht1 > gewicht2:
    naam = naam1
else:
    naam = naam2

if bmi < 18.5:
    indicatie = 'heeft ondergewicht'
elif 18.5 <= bmi < 25:
    indicatie = 'heeft een gezond gewicht'
elif 25 <= bmi <30:
    indicatie = 'heeft overgewicht'
else:
    indicatie = 'is obees'

#formattering
mes = '{} heeft het hoogste BMI ({:.2f}) en {}.'.format(naam, bmi, indicatie)

#uitvoer
print(mes)