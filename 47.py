from tools.primes import prime_factors_of, primes_under, is_prime
from tools.collections import mil_primes, mil_primes_dict
from more_itertools import consecutive_groups
import numpy as np




quad_prime_factors = []

for hd in range(50):
    print(hd * 100000 , "reached")
    for n in range(hd * 100000, (hd + 1) * 100000):
        factors = prime_factors_of(n)
        if len(factors) > 3:
            quad_prime_factors.append(n)

    cqpf = [list(item) for item in consecutive_groups(quad_prime_factors)]
    cqpf = [i for i in cqpf if len(i) > 3]
    if len(cqpf):
        print(cqpf)
        break
    else:
        quad_prime_factors = quad_prime_factors[-5:]
    
