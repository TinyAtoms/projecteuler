
last_ten = 0
for i in range(1,1001):
    last_ten += pow(i,i, 10000000000)
    print(i)

print(last_ten)