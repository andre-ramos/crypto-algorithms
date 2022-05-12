import math
import random


def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True

def get_ptime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


print(get_ptime(3))