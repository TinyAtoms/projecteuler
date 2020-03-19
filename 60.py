from tools.collections import mil_primes, bil_primes
from tools.primes import is_prime
import numpy as np
'''
it took 4 mins. idk if it counts
'''


thousands = mil_primes[mil_primes<10000]
thousands = thousands.astype(str)


print("begin pairs")
pairs = []
for i in range(thousands.size):
    for j in range(i, thousands.size):
        a = thousands[i]
        b = thousands[j]
        if is_prime(int(a + b)) and is_prime(int(b + a)):
            pairs.append((a,b))

print("Begin triplets")
triplets = []
for i in thousands:
    for p in pairs:
        if is_prime(int(i + p[0])) and is_prime(int(p[0] + i)) and is_prime(int(i + p[1])) and is_prime(int(p[1] + i)):
            if i not in p:
                triplets.append((p[0], p[1], i))


print("begin quadruplets")
quads = []
for i in thousands:
    for p in triplets:
        if is_prime(int(i + p[0])) and is_prime(int(p[0] + i)) and is_prime(int(i + p[1])) and is_prime(int(p[1] + i)):
            if is_prime(int(i + p[2])) and is_prime(int(p[2] + i)) and i not in p:
                quads.append((p[0], p[1], p[2], i))



print("begin pentuplets")
pentas = []
for i in thousands:
    for p in quads:
        if is_prime(int(i + p[0])) and is_prime(int(p[0] + i)) and is_prime(int(i + p[1])) and is_prime(int(p[1] + i)):
            if is_prime(int(i + p[2])) and is_prime(int(p[2] + i)) and i not in p and is_prime(int(i + p[3])) and is_prime(int(p[3] + i)):
                pentas.append((p[0], p[1], p[2], p[3], i))


answer = [[int(i) for i in b] for b in pentas]
answer = sorted(answer, key=sum)
print(sum(answer[0]), answer[0])
