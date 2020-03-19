import numpy as np
from collections import defaultdict
'''
plan of attack:
precalculate the first 1k cubes
then make a dict where the key is the sorted digits of a number, and the value is a list of all the numbers that contain those digits
eg 
dict[234] = [234, 243, 324, 342, 423, 432]
then simply return the smallest value where i only have 5 numbers
'''
numbers = np.arange(1, 10000)
numbers = numbers * numbers * numbers
numbers = numbers.astype(str)


numdict = defaultdict(list)

for i in numbers:
    n = "".join(sorted(i))
    numdict[n].append(i)


for k, v in numdict.items():
    if len(v) == 5:
        print(min([int(i) for i in v]))



