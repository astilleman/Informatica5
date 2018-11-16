#for i in range(10):
    #print(i)

#geeft 10 getallen, in informatica altijd begin 0
#stop is niet meer
##################################
#for i in range(10, 0, -1):
    #print(i)

#print('Raket vertrekt')
####################################"
#for _ in range(10, 0, -1):
    #print('k')

#print('Raket vertrekt')
###################################


#\n is new line
#\t is een tab

n = int(input('getal: ')) cijfers, ontbreken = '', ''
for i in range(1, 11):     cijfers += str(n * i)
for c in '0123456789':     if c not in cijfers:         ontbreken += c
if len(ontbreken) == 0:     print('Tafel van ' + str(n) + ' is een mooie tafel') else:     print('In de tafel van ' + str(n) + ' ontbre(e)k(t)en ' + ontbreken