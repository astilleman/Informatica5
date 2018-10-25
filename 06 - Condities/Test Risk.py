a1 = int(input('a1: '))
a2 = int(input('a2: '))
a3 = int(input('a3: '))
v1 = int(input('v1: '))
v2 = int(input('v2: '))

#sorteren
sa1 = max(a1, a2, a3)
sa2 = a1 + a2 + a3 - sa1 -min(a1, a2, a3)
print(sa1, sa2)

sv1 = max(v1, v2)
sv2 = min(v1, v2)
print(sv1, sv2)

#winnaar bepalen
if sa1 > sv1 and sa2 > sv2:
    mes = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif sv1 >= sa1 and sv2 >= sa2:
    mes = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'
else:
    mes = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

#uitvoer
print(mes)