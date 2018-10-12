#invoer
ogen_a1 = int(input('Geef aantal ogen dobbelsteen 1 aanvaller: '))
ogen_a2 = int(input('Geef aantal ogen dobbelsteen 2 aanvaller: '))
ogen_a3 = int(input('Geef aantal ogen dobbelsteen 3 aanvaller: '))
ogen_v1 = int(input('Geef aantal ogen dobbelsteen 1 verdediger: '))
ogen_v2 = int(input('Geef aantal ogen dobbelsteen 2 verdediger: '))

#aantal ogen dobbelstenen
max_1_ogen_a = max(ogen_a1, ogen_a2, ogen_a3)
max_2_ogen_a = min(max(ogen_a1, ogen_a2), max(ogen_a1, ogen_a3), max(ogen_a2, ogen_a3))
max_ogen_v = max(ogen_v1, ogen_v2)
min_ogen_v = min(ogen_v1, ogen_v2)

#aanvallen
if max_1_ogen_a > max_ogen_v and max_2_ogen_a > min_ogen_v:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
elif max_1_ogen_a > max_ogen_v or max_2_ogen_a > min_ogen_v:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
else:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')






