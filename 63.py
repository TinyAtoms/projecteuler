'''
attack:
make a list with n digits
keep generating a list where a^i for i in range(1,m) and a in previously mentioned list
append values to total list whenever len(str(j)) == i for j in last mentioned list
print length of total list
'''

total = []

multiplier = range(1,50)
numbers = [1 for i in range(49)]

count = 0
for i in range(1,50):
    old = len(total)
    numbers = [a*b for a,b in zip(numbers, multiplier)]
    temp = [str(a) for a in numbers]

    for a,  j in enumerate(temp):
        if len(j) == i:
            total.append((j, "{}^{}".format(multiplier[a], i)))
    if old == len(total):
        count +=1
        if count == 5:
            break
print(total, len(total))
