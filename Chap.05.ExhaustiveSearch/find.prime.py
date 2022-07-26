def find_primes(n):
    sieve = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 0:
            for j in range(i * i, n + 1, i):
                sieve[j] = 1
    return [i for i in range(2, n + 1) if sieve[i] == 0]

print(find_primes(10))
print(find_primes(100))