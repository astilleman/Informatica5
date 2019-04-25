# bestand = open('klas.txt')
#
# lijn = bestand.readline()
#
# while lijn != '':
#     print(lijn)
#     lijn = bestand.readline()
#
# print(lijn)
#
# bestand.close()

# lijnen = []
#
# with open('klas.txt') as bestand:
#     lijnen = bestand.readlines()

#print(lijnen)

#for naam in lijnen:
    #print(naam[::-1])

#print('er zitten ' + str(len(lijnen)) + ' personen in de klas')

nieuwe_leerlingen = ['Alice', 'Baptiste']

with open('klas.txt', 'a') as bestand:
    #bestand.writeline('\n' + '\n'.join(nieuwe_leerlingen))
    bestand.writelines(nieuwe_leerlingen)
