

digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

n_digits = sum([len(i) for i in digits])

unique = [
    "ten",
    "eleven",
    "twelvethirteenfourteenfifteensixteen",
    "seventeeneighteennineteen"
]
unique = sum([len(i) for i in unique])

# 20-30 is twenty x, twenty x, etc. 10x 'twenty' plus length of digits
# this continues untill one hundred

teens = [
    "twenty",
    "thirty",
    "fourty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

# 1-9 + 10-19 + 20-99
total_hundred = unique + n_digits + 9 * (sum([len(i) for i in teens]) + n_digits) + 1

# hundreds is X hundred and Y, so total_hundred + 99 * (X hundred and) + X hundred 
total_thousand = total_hundred
for i in digits:
    temp = total_hundred + (len(i) + len("hundredand")) * 100 - 3 
    total_thousand += temp

total_thousand += len("onethousand")
print(total_thousand)
print(total_hundred)