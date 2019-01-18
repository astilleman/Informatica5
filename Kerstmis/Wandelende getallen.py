#invoer
getal = str(input('Geef een getal in tekstvorm: '))

#bewerking
from math import radians, sin, cos
x_coördinaat, y_coördinaat = 0, 0
for i in getal:
    if i == '0':
        y_coördinaat += 1
    elif i == '1':
        x_coördinaat += sin(radians(36))
        y_coördinaat += cos(radians(36))
    elif i == '2':
        x_coördinaat += sin(radians(72))
        y_coördinaat += cos(radians(72))
    elif i == '3':
        x_coördinaat += sin(radians(108))
        y_coördinaat += cos(radians(108))
    elif i == '4':
        x_coördinaat += sin(radians(144))
        y_coördinaat += cos(radians(144))
    elif i == '5':
        y_coördinaat -= 1
    elif i == '6':
        x_coördinaat += sin(radians(216))
        y_coördinaat += cos(radians(216))
    elif i == '7':
        x_coördinaat += sin(radians(252))
        y_coördinaat += cos(radians(252))
    elif i == '8':
        x_coördinaat += sin(radians(288))
        y_coördinaat += cos(radians(288))
    elif i == '9':
        x_coördinaat += sin(radians(324))
        y_coördinaat += cos(radians(324))

#formattering
message = 'Getal {} wandelt naar positie ({:.2f}, {:.2f}).'.format(getal, x_coördinaat, y_coördinaat)

#uitvoer
print(message)

######################################################################################################korter

#invoer
g = float(input('Geef een kommagetal: '))

#berekening
from math import sin, cos, radians
x_coördinaat, y_coördinaat = 0, 0
g = str(g)
for i in range(len(g)):
    if 48 <= ord(g[i]) <= 57:
        x_coördinaat += sin(radians(int(g[i]) * 36))
        y_coördinaat += cos(radians(int(g[i]) * 36))

#formattering
message = 'Getal {} wandelt naar positie ({:.2f}, {:.2f}).'.format(g, x_coördinaat, y_coördinaat)

#uitvoer
print(message)