#berekening
woord = str(input('Geef een woord: '))
gedraaide_bedrag = int(input('Geef het gedraaide geldbedrag: '))
letter = str(input('Geef een letter: '))
gewonnen_bedrag = 0
genoemde_letters = ''
mes = ''

while letter in woord and letter not in genoemde_letters:
    gewonnen_bedrag += gedraaide_bedrag
    genoemde_letters += letter
    letter = str(input('Geef een letter: '))

mes = gewonnen_bedrag

#uitvoer
print(gewonnen_bedrag)