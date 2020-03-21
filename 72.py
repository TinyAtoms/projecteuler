# from tools.math import gcd
# from tools.primes import prime_factors_of
# from tools.collections import mil_primes_dict, mil_primes
# from sympy.ntheory.factor_ import totient as phi
# from math import sqrt

'''
fool's graveyard
1.
compute all prime factors of n <1000001
for i in 1m, for j in range(1,i)
common factors = intersection of i and j from precomputed results
high factor is the multiplication of all common factors
append (j/hi, i,hi) to set
2. 
the sum of all n < d where you get a proper fraction n/d is all n < d where gcd(n,d) ==1. 
that's phi function.
So we want the sum of phi(i) for all i <= 1000000

'''

proper_count = 0
for i in range(2,1000001):
    proper_count += phi(i)

print(proper_count)
