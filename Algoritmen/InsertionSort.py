from time import time
from random import randint
import matplotlib.pyplot as plt

def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a

i, n, t = 10, [], []

while i < 10000:

    rij = genereer_rij(i)

    start = time()
    rij = insertion_sort(rij)
    stop = time()

    n.append(i)
    t.append(stop - start)

    i *= 2

plt.plot(n , t, '-ro')
plt.title('insertion sort')
plt.xlabel('N')
plt.ylabel('t')
plt.show()



