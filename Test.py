def vlag(richting, kleuren):
    flag = kleuren[0]
    for kleur in kleuren[1:]:
        if richting == 'horizontaal':
            flag += '\n-\n' + kleur
        elif richting == 'verticaal':
            flag += ' | ' + kleur
    return flag

print(vlag('verticaal', ('zwart', 'geel', 'rood')))
print(vlag('horizontaal', ('rood', 'wit', 'blauw')))