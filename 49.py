from tools.primes import primes_under

thousands_prime = primes_under(10000)
thousands_prime = thousands_prime[thousands_prime > 999]
# ^replace this with your sieve and then eliminate every prime under 1000

prime_digits = {}
primes = [[],[],[],[],[]]
for i in thousands_prime:
    a = set([d for d in str(i)])
    if len(a) > 2:
        prime_digits[i] = a
        primes[len(a)].append(i)

print("done with hashing")

groups = []
for ndigit in [2,3,4]:
    pr = primes[ndigit]
    for a, n1 in enumerate(pr):
        for b, n2 in enumerate(pr[a+1:]):
            for n3 in pr[a+b+2:]:
                if prime_digits[n1] == prime_digits[n2] and prime_digits[n2] == prime_digits[n3]:
                    groups.append([n1, n2, n3])
    print("done with digits:", ndigit)

for group in groups:
    group = sorted(group)
    if group[1] - group[0] == group[2] - group[1]:
        print(group)
