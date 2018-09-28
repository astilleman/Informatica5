constante_van_Avogadro = 6.020 * (10 ** 23)
molaire_massa_zwavel = 32.06

#invoer
aantal_mol_zwavel = float(input('Geef aantal mol S: '))

#berekening
massa_zwavel = (molaire_massa_zwavel) * (aantal_mol_zwavel)
aantal_deeltjes_zwavel = (aantal_mol_zwavel) * (constante_van_Avogadro)

print(massa_zwavel)
print(aantal_deeltjes_zwavel)

