def nieuw_kaartspel(kleuren, waarden):
    nieuwe_lijst = []
    for i in range(len(kleuren)):
        for j in range(len(waarden)):
            nieuwe_lijst.append(kleuren[i] + waarden[j])

    return nieuwe_lijst

#print(nieuw_kaartspel(['blad ', 'steen ', 'schaar '],['1', '2', '3']))

def splits_kaartspel(kaartenlijst):
    return kaartenlijst[:len(kaartenlijst) // 2], kaartenlijst[len(kaartenlijst) // 2:]

#print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))

def faro_shuffle(kaartenlijst1, kaartenlijst2):
    nieuwe_lijst = []
    for i in range(len(kaartenlijst1)):
        nieuwe_lijst.append(kaartenlijst1[i])
        nieuwe_lijst.append(kaartenlijst2[i])
    if len(kaartenlijst2) > len(kaartenlijst1):
        nieuwe_lijst.append(kaartenlijst2[len(kaartenlijst1)])

    return nieuwe_lijst


#print(faro_shuffle(['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HB', 'HD', 'HH', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RB', 'RD', 'RH'],['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'KB', 'KD', 'KH', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SB', 'SD', 'SH']))


