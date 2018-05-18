from random import seed
from random import randrange

def gener_random_seq(n):
    L = []
    for i in range(n):
        L.append(randrange(1, 10000))
    return L

