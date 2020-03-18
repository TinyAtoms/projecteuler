from tools.primes import factors_of
import numpy as np

def is_abundant(n):
    sumn = sum(factors_of(n)[:-1])
    return sumn > n
'''
plan of attack:
gen all abundant numbers till 28K
then do for all i,j in the abundant numbers, store the sums of those
then filter a range till 28k with those sums, and then sum out the leftovers
'''

numbers = np.arange(1,28123) 
abundant_ns = []
for i in numbers:
    if is_abundant(i):
        abundant_ns.append(i)
abundant_ns = np.array(abundant_ns)

# use set to remove duplicates. Also, theoretically, existence checking in a set should be faster than array
sum_abundants = set([])
for i in abundant_ns:
    temp = np.full(abundant_ns.size, i)
    temp = temp + abundant_ns
    sum_abundants =sum_abundants.union(temp)

# welp, np.in1d doesn't want to play nice with sets. 
sum_abundants = np.array(list(sum_abundants))
ar_filter =np.logical_not( np.in1d(numbers, sum_abundants))
numbers = numbers[ar_filter]
print(sum(numbers))

    



