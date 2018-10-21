#invoer
a = int(input('Geef a: '))
b = int(input('Geef b: '))

#exponenten van 10
i1= 0
i2= 1
i3= 2
i4= 3
i5= 4

#factor van a en b
x1 = pow(10, i1)
x2 = pow(10, i2)
x3 = pow(10, i3)
x4 = pow(10, i4)
x5 = pow(10, i5)

#berekening
c1 = (x1 * a) + (x1 * b)
c2 = (x2 * a) + (x2 * b)
c3 = (x3 * a) + (x3 * b)
c4 = (x4 * a) + (x4 * b)
c5 = (x5 * a) + (x5 * b)

#tussenuitvoer en uitvoer
tu1 = '{:>6d} + {:<6d} = '.format((x1 * a), (x1 * b))
tu2 = '{:>6d} + {:<6d} = '.format((x2 * a), (x2 * b))
tu3 = '{:>6d} + {:<6d} = '.format((x3 * a), (x3 * b))
tu4 = '{:>6d} + {:<6d} = '.format((x4 * a), (x4 * b))
tu5 = '{:>6d} + {:<6d} = '.format((x5 * a), (x5 * b))

u1 = tu1 + str(c1)
u2 = tu2 + str(c2)
u3 = tu3 + str(c3)
u4 = tu4 + str(c4)
u5 = tu5 + str(c5)

print(u1)
print(u2)
print(u3)
print(u4)
print(u5)

#a, b, a + b * 10, *100, *1000,*10000 telkens
###########################################################################################

#invoer
a = int(input('Geef a: '))
b = int(input('Geef b: '))

#berekening
som1 = a + b
som2 = (a + b) * 10
som3 = (a + b) * 100
som4 = (a + b) * 1000
som5 = (a + b) * 10000

#formattering
print('{:>6d} + {:<6d} = {}'.format(a, b, som1))
print('{:>6d} + {:<6d} = {}'.format(a * 10, b * 10, som2))
print('{:>6d} + {:<6d} = {}'.format(a * 100, b * 100, som3))
print('{:>6d} + {:<6d} = {}'.format(a * 1000, b * 1000, som4))
print('{:>6d} + {:<6d} = {}'.format(a * 10000, b * 10000, som5))