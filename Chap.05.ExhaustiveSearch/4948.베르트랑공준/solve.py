def find_primes(m):
    n = 2*m
    sieve = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 0:
            for j in range(i * i, n + 1, i):
                sieve[j] = 1
    return [i for i in range(m + 1, n + 1) if sieve[i] == 0]

while True:
    n = int(input())
    if n == 0: break
    print(len(find_primes(n)))