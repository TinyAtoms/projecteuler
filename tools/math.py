from functools import lru_cache
from math import gcd




@lru_cache
def factorial(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res


def combination_length(n, r):
    return int(factorial(n) / (factorial(n-r) * factorial(r)))