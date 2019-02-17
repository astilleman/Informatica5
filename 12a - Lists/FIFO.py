# niet ? niet controleren
invoer = input('invoer:')
queue = []

while invoer != 'STOP':

    if invoer != '?':
        queue.append(invoer)

    elif len(queue) > 0:
        print(queue.pop(0))

    invoer = input('invoer: ')


#############################################
'''#invoer
invoer = input('Geef een invoer: ')

#berekening
lijst = []
while invoer != 'STOP':
    if invoer != '?':
        lijst.append(invoer)
    elif invoer != []:
        print(lijst.pop(0))
    invoer = input('Geef een invoer: ')'''

