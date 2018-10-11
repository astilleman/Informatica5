hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee)')

if hendel_trekken == 'ja':

    man_duwen = input('Man van de brug duwen? (ja/nee)')

    if man_duwen == 'ja':
        doden = 2
    else:
        doden = 1


else:

    man__duwen = input('Man van de brug duwen? (ja/nee)')

    if man__duwen == 'ja':
        doden = 1
    else:
        doden = 5

print(doden)

