#invoer
e = int(input('Geef aantal elektronen in atoom: '))

#formattering
zin= 'De {}-schil is de buitenste schil van een stabiel atoom met {} elektronen.'

#berekening
if 1 <= e <= 2:
    print(zin.format('K', e))
elif 2 < e <= 10:
    print(zin.format('L', e))
elif 10 < e <= 28:
    print(zin.format('M', e))
elif 28 < e <= 60:
    print(zin.format('N', e))
elif 60 < e <= 92:
    print(zin.format('O', e))
elif 92 < e <= 124:
    print(zin.format('P', e))
elif 124 < e <= 156:
    print(zin.format('Q', e))