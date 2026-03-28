def prime_generator():
    primes = []
    n = 2
    while True:
        if all(n % p != 0 for p in primes):
            primes.append(n)
            yield n
        n += 1

gen = prime_generator()
for prime in gen:
    print(prime)
