from tools.math import gcd
from tools.primes import prime_factors_of
from tools.collections import mil_primes_dict, mil_primes
from sympy.ntheory.factor_ import totient as phi
from math import sqrt
'''
the naive fool's  ideas graveyard.
1.
phi = sum([1 for i in range(1,n) if gcd(i,n) == 1 ]
2. 
get prime factors. 
get all multiples of those factors under n.
return (n -1) - len(factor multiples)
3. precalculate phi for products of primes and phi for n^k for primes(about 66% of all primes), then slowly calculate the others
4. realize scipy has a faster(50x) phi function than whatever you wrote

'''



phin = {

}

temp = mil_primes[mil_primes < 500000]
older_temp = temp
for i in range(2,11):
    temp = temp * mil_primes[:temp.size]
    other_mul = mil_primes[:temp.size] - 1
    result = other_mul * older_temp
    older_temp = temp
    for i in range(temp.size):
        phin[temp[i]] = result[i]

mil_primes = list(mil_primes)
for i, num in enumerate(mil_primes):
    for j in mil_primes[i+1:]:
        phin[num] = num - 1
        prod = num * j
        if prod > 1000000:
            break
        phin[prod] = (num -1) * (j - 1)
    if not num % 100:
        print(num)


maxres = [0,0] # i, phidiv
for i in range(30000,1000000):
    if i in phin:
        phii = phin[i]
    else:
        phii = phi(i)
    phidiv = i / phii
    if phidiv > maxres[1]:
        maxres = [i, phidiv]
        print("newmax", maxres)
print("max", maxres)


