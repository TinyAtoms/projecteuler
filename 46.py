from tools.primes import primes_under
from tools.collections import mil_primes
import numpy as np


ns = np.arange(1, 1000000)
double_squares = ns * ns * 2
double_squares = double_squares[double_squares < 1000000]


def other_golbach(n):
    primes = primes_under(n)
    ds = double_squares[double_squares < n]
    for i in primes:
        if n in ds + i:
            return True
    return False

odd = np.arange(3,1000000, 2)
odd_composite = odd[np.isin(odd, mil_primes) == False]

for i in odd_composite:
    if not other_golbach(i):
        print(i)
        break