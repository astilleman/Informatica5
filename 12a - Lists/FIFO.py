# niet ? niet controleren
invoer = input('invoer:')
queue = []

while invoer != 'STOP':

    if invoer != '?':
        queue.append(invoer)

    elif len(queue) > 0:
        print(queue.pop(0))

    invoer = input('invoer: ')

