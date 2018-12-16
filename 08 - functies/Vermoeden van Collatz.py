def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend_getal = n // 2
    else:
        volgend_getal = (n * 3) + 1
    return volgend_getal

def collatz(n):
    cyclelengte = 1
    while n > 1:
        cyclelengte += 1
        n = volgend_collatz_getal(n)
    return cyclelengte





#alles kopiëren behalve print