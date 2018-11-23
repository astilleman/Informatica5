def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend_getal = n // 2
    else:
        volgend_getal = (n * 3) + 1
    return(volgend_getal)

print(volgend_collatz_getal())

def collatz(n):
    while n <
#alles kopiëren behalve print