from tools.math import gcd
from fractions import Fraction

fractions = [Fraction(3,7)]

smallest_frac = Fraction(3,7)
for d in range(1,1000000):
    n = int(smallest_frac * d)
    while True:
        if gcd(n,d) == 1:
            fractions.append(Fraction(n,d))
            # print(n,d)
            break
        else:
            n -=1
    if not n % 50000:
        print(n)
        
fractions = sorted(fractions)
index = fractions.index(smallest_frac)
print(fractions[index - 10:index+2])




