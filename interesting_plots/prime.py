

import itertools
from sympy import sieve
from math import sqrt, ceil
import numpy as np
from datetime import datetime


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = list(func(*args, **kwargs))
#         # result = func(*args, **kwargs)
#         end = datetime.now()
#         print(func.__qualname__, args, "took \t\t",
#               (end-start).microseconds/1000, "milliseconds")
#         return result
#     return wrapper


def timer_noresult(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = list(func(*args, **kwargs))
        # result = func(*args, **kwargs)
        end = datetime.now()
        # print(func.__qualname__, args, "took \t\t",
        #       (end-start).microseconds/1000, "milliseconds")
        return (end-start).total_seconds() * 1000
    return wrapper


def sieveOfAtkin(end):
    """sieveOfAtkin(end): return a list of all the prime numbers <end
    using the Sieve of Atkin."""
    # Code by Steve Krenzel, <Sgk284@gmail.com>, improved
    # Code: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
    # Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
    assert end > 0
    lng = ((end-1) // 2)
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end-1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not(n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end:
            y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[:max(0, end-2)]

    for n in range(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s = int(sqrt(end)) + 1
    if s % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])

    return primes


def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


# new
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=np.bool)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i & 1)+4)//3::2*k] = False
    return np.r_[2, 3, ((3*np.nonzero(sieve)[0][1:]+1) | 1)]


def symsieve(n):
    return list(sieve.primerange(1, n))


izip = itertools.zip_longest
chain = itertools.chain.from_iterable
compress = itertools.compress


def rwh_primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    zero = bytearray([False])
    size = n//3 + (n % 6 == 2)
    sieve = bytearray([True]) * size
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            start = (k*k+4*k-2*k*(i & 1))//3
            sieve[(k*k)//3::2*k] = zero*((size - (k*k)//3 - 1) // (2 * k) + 1)
            sieve[start::2*k] = zero*((size - start - 1) // (2 * k) + 1)
    ans = [2, 3]
    poss = chain(izip(*[range(i, n, 6) for i in (1, 5)]))
    ans.extend(compress(poss, sieve))
    return ans


# to be tested


# n = int(input("input n:"))
# res1 = erato_test(n)
# res2 = atkin_test(n)
# res3 = primes_test(n)
# res4 = primes1_test(n)
# res5 = primesfrom3to_test(n)
# res6 = primesfrom2to_test(n)
# res7 = symsieve_test(n)
# res8 = rwh_primes2_test(n)



if __name__ == "__main__":
    import json
    from collections import defaultdict
    erato_test = timer_noresult(eratosthenes2)
    atkin_test = timer_noresult(sieveOfAtkin)
    primes_test = timer_noresult(primes)
    primes1_test = timer_noresult(primes1)
    primesfrom3to_test = timer_noresult(primesfrom3to)
    primesfrom2to_test = timer_noresult(primesfrom2to)
    symsieve_test = timer_noresult(symsieve)
    rwh_primes2_test = timer_noresult(rwh_primes2)
    n_list = [2000, 4000, 6000, 8000, 10000,
    20000, 40000, 60000, 80000, 100000,
    200000, 400000, 600000, 800000, 1000000,
    2000000, 4000000, 6000000, 8000000, 10000000,
    15000000, 20000000, 25000000, 30000000
    ]
    functions = [erato_test, atkin_test, primes_test,primes1_test,  primesfrom3to_test, primesfrom2to_test, symsieve_test, rwh_primes2_test]
    fun_names = ["erato", "atkin", "primes", "primes1", "primesfrom3to", "primesfrom2to", "siemsieve", "rwh_primes2"]
    results = {}

    for i, funct in enumerate(functions):
        print(fun_names[i])
        temp_list = []
        for n in n_list:
            temp_list.append(funct(n))
        results[fun_names[i]] = temp_list
        print(temp_list)

    with open("results.json", "w") as resf:
        json.dump(results, resf)


