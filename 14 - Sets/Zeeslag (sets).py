def boot_overlappend(co1, co2):
    return len(co1.intersection(co2)) != 0

#print(boot_overlappend({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))

def boot_toevoegen(co1, co2):
    if boot_overlappend(co1, co2) is False:
        mes = co1.union(co2)
    else:
        mes = co2
    return mes

#print(boot_toevoegen({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
#print(boot_toevoegen({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))

def vuur(vakje, co):
    parameter = set(vakje.split())
    if parameter.issubset(co) is True:
        mes = True
        co.remove(vakje)

    else:
        mes = False
    return mes, co

#print(vuur('I7',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))
#print(vuur('F8',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))
