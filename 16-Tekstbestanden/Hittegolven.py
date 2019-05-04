def to_int_temp(lijn):
    int_lijn = []
    lijn = lijn.split()

    for t in lijn:
        int_lijn.append(int(t))

    return int_lijn

lijnen = []

with open('temperaturen.txt') as bestand:
   lijnen = bestand.readlines()

dag = 0
aantal_25_plus = 0
aantal_30_plus = 0
hittegolven = []

for lijn in lijnen:

    temp = to_int_temp(lijn)
    print(temp)

    for i in range(len(temp)):

        #hoger dan 30
        if temp[i] >= 30:
            aantal_30_plus += 1
            aantal_25_plus += 1

        #hoger dan 25
        elif temp[i] >= 25:
            aantal_25_plus += 1

        #lager dan 25
        else:
            # was vorige periode hittegolf? --> ja , sla op
            if aantal_25_plus >= 5 and aantal_30_plus >= 3:
                #ja , sla op
                hittegolven.append((dag - aantal_25_plus, dag))

            #periode op nul zetten
            aantal_30_plus, aantal_25_plus = 0, 0
    dag += 1

#laatste periode een hittegolf?
if aantal_25_plus >= 5 and aantal_30_plus >= 3:
    # ja , sla op
    hittegolven.append((i - aantal_25_plus, i))

print(hittegolven)




