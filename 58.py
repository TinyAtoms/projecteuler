from tools.primes import is_prime
from tools.math import factorial
from math import sqrt
from functools import lru_cache

'''
here are the diagonals for a given sidelength n:
n = 1 : 1
n = 3: 3,5,7,9 + diags(n-2)
n = 5 : 13, 17, 21, 25, diags(n-2)
n = 7 : 31, 37, 43, 49, diags(n-2)
n=9 : 57, 65, 73, 81 + diags(n-2)
The following pattern is spotted:
m = max(diags(n-2))
diags(n) = m + (n-1), m + 2(n-1), m + 3(n-1),m + 4(n-1), diags(n-2)
So, we can generate the diagonals for a given side length now.
So, keep generating diagonals for increasing sidelenths and calculate the prime ratio
'''


@lru_cache
def gen_numbers(n):
    if n == 1:
        return [1]
    last = gen_numbers(n-2)
    nextdiags = [max(last) + i * (n -1) for i in range(1,5)]
    diags = nextdiags
    return diags

gen_numbers(1)

primes = 0
for i in range(3,30000, 2):
    nums = gen_numbers(i)
    primes += len([i for i in nums if is_prime(i)])
    primeratio = primes/ (2 * i - 1)
    if i % 1000 == 1:
        print(i, "{}/{} = {}".format(primes, (2 * i - 1), primeratio))
    if primeratio < 0.1:
        print(nums[:4])
        break
        