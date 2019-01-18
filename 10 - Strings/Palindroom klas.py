def palindroom(woord):

    #return woord == woord[::-1] ook test palindroom en eigenlijk beter
    i = 0

    while woord[i] == woord[-i - 1] and i < len(woord) // 2:
        i += 1

    return i == (len(woord) // 2)

print(palindroom('ab' + (100000000 * 'a')))