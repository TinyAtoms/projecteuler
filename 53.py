
from tools.math import factorial



def combination_len(n, cutoff=1000000):
    total = 0
    for i in range(1, n):
        temp = factorial(n) / (factorial(n-i) * factorial(i))
        if temp > cutoff:
            total +=1
    return total


total = 0
for i in range(1, 101):
    total += combination_len(i)

print(total)