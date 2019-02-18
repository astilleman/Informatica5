def vlag(richting, kleuren):
    message = kleuren[0]
    if richting == 'horizontaal':
        for kleur in kleuren[1:]:
            message += '\n' + '-\n' + kleur

    elif richting == 'verticaal':
        for kleur in kleuren[1:]:
            message += ' ' + '| ' + kleur #' | '

    return message

print(vlag('verticaal',('zwart', 'geel', 'rood')))