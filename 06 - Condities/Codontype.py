#invoer
RNA_codon = str(input('Geef het RNA codon: '))

#formattering
zin = 'Het codon {} is een {} codon.'

#berekening
if RNA_codon == 'AUG':
    print(zin.format(RNA_codon, 'start'))
elif RNA_codon == 'UAG' or RNA_codon == 'UGA'or RNA_codon == 'UAA':
    print(zin.format(RNA_codon, 'stop'))
elif len(RNA_codon) == 3:
    print(zin.format(RNA_codon, 'gewoon'))
else:
    print(zin.format(RNA_codon, 'ongeldig'))