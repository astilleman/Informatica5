#invoer
uur_vertrek_thuis = int(input('Geef uur vertrek thuis: '))
minuten_vertrek_thuis = int(input('Geef minuten vertrek thuis: '))
uur_aankomst_bij_vriendin = int(input('Geef uur aankomst bij vriendin: '))
minuten_aankomst_bij_vriendin = int(input('Geef minuten aankomst bij vriendin: '))
uur_vertrek_van_vriendin = int(input('Geef uur vertrek van vriendin: '))
minuten_vertrek_van_vriendin = int(input('Geef minuten vertrek van vriendin: '))
uur_aankomst_thuis = int(input('Geef uur aankomst thuis: '))
minuten_aankomst_thuis = int(input('Geef minuten aankomst thuis: '))

#berekening reistijd heen of terug
resultaat = ((1440 - (uur_vertrek_thuis * 60 + minuten_vertrek_thuis)) + (uur_aankomst_thuis * 60 + minuten_aankomst_thuis)) % 1440
resultaat -= ((1440 - (uur_aankomst_bij_vriendin * 60 + minuten_aankomst_bij_vriendin)) + (uur_vertrek_van_vriendin * 60 + minuten_vertrek_van_vriendin)) % 1440
resultaat /= 2


#berekening tijdstip
correcte_minuten_aankomst_thuis = int((minuten_vertrek_van_vriendin + (resultaat % 60)) % 60)
correcte_uur_aankomst_thuis = int(((uur_vertrek_van_vriendin + (resultaat // 60)) + ((minuten_vertrek_van_vriendin +resultaat % 60)) // 60) % 24)
print(correcte_uur_aankomst_thuis)
print(correcte_minuten_aankomst_thuis)

#15:45 945   18:05 1085     140
# 16:30  990   17:14  1024    34
# 53
# python console gebruiken als rekenmachine
#21 14 11 45 22 58 14 59       2 14
#15 1 17 5 18 1 18 23     19 14
#557213823281659284





