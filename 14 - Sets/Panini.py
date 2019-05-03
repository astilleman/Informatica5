def verzamel(naam, stickerboek, dubbels):
    speler = set(naam.split())
    nieuw_stickerboek = stickerboek.union(speler)
    if nieuw_stickerboek == stickerboek and len(dubbels) > 0:
        i = 1
        mes = 'OK'
        while i <= max(dubbels) and mes != 'STOP':
            if i in dubbels and naam in dubbels[i]:
                if i + 1 in dubbels:
                    dubbels[i + 1].add(naam)
                else:
                    dubbels[i + 1] = {naam}
                if len(dubbels[i]) > 1:
                    dubbels[i].discard(naam)
                else:
                    dubbels.pop(i)
                mes = 'STOP'
            else:
                i += 1
        if i == max(dubbels) + 1:
            if 1 in dubbels:
                dubbels[1].add(naam)
            else:
                dubbels[1] = {naam}
    elif nieuw_stickerboek == stickerboek:
        dubbels[1] = {naam}

    return nieuw_stickerboek, dubbels

print(verzamel('Bosmans',{'Bosmans', 'Weber'},{1: {'Bosmans'}}))

