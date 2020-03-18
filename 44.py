from collections import defaultdict

def pentagonal(n):
    return int((3 * n ** 2 - n) / 2)





pentagon_numbers = defaultdict(bool)
pentagonal_list = []
# list for itterating over numbers, dict for checking existence
for i in range(1, 10000):
    pentagonal_list.append(pentagonal(i))
for i in pentagonal_list:
    pentagon_numbers[i] = True

D = 1000000000 # arbitratily chosen
for index, j in enumerate(pentagonal_list):
    for k in pentagonal_list[index:]:
        diff = k - j
        if diff > D: # time to break innermost loop, all next D will be bigger
            break
        if pentagon_numbers[diff] and pentagon_numbers[k + j] and D > diff:
            D = diff
            print("j", j, "k", k)

print(D)