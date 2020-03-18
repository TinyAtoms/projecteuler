import numpy as np
import builtins

def digitsum(n):
    return sum([int(i) for i in str(n)])



multiplier = list(range(1,100))
nums = [1 for i in multiplier]
maxsum = 0
for i in multiplier:
    for j, val in enumerate(nums):
        temp = val * multiplier[j]
        nums[j] = temp
        digits = digitsum(temp)
        if digits > maxsum:
            maxsum = digits

    # print(nums)
print(maxsum)