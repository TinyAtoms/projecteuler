import numpy as np

powers = {}

max_check = 0
for i in range(10):
    temp = pow(i,5)
    powers[str(i)] = temp
    max_check += temp


total = 0
for i in range(2,max_check * 2):
    powersum = sum([powers[a] for a in str(i)])
    if i == powersum:
        total += powersum
        print(i, total)
