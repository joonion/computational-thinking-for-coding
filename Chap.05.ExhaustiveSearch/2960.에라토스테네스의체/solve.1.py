def find_primes(n):
    sieve = [i for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * i, n + 1, i):
            sieve[j] = 0
    primes = []
    for i in range(2, n + 1):
        if sieve[i] != 0:
            primes.append(i)
    return primes
        
def solve(n, k):
    primes = find_primes(n)
    print(primes)
    return primes[k - 1]

N, K = map(int, input().split())
print(solve(N, K))