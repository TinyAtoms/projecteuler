from fractions import Fraction


its = {1: Fraction(1,2)}

for i in range(1, 1001):
    temp = its[i] + 2
    temp2 = Fraction(temp._denominator, temp._numerator)
    its[i+1] = temp2

count = 0
for i in range(1,1001):
    temp = its[i] + 1
    if len(str(temp._numerator)) > len(str(temp._denominator)):
        print(temp, "OK")
        count += 1
print(count)
