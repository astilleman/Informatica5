def is_palindroom(woord):
    message = ''
    for i in range(0, len(woord)):
        if woord[i] != woord[len(woord) - (i + 1)]:
            message = False
    if message != False:
        message = True
    return message


print(is_palindroom('x'))

