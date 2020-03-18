from tools.collections import mil_primes_dict, mil_primes
from numpy import sum


prime = 2
consecutive = 499
print(mil_primes.size)
while consecutive < 1000:
    check = prime
    for i in range(mil_primes.size - consecutive):
        temp_range = mil_primes[i:i+consecutive]
        possible_prime = sum(temp_range)
        if possible_prime in mil_primes_dict:
            prime = possible_prime
            print("range between {} and {} ({} consecutives) makes {}".format(temp_range[0], temp_range[-1], consecutive, prime))
            break
    consecutive += 1
    print("consecutive increased", consecutive)