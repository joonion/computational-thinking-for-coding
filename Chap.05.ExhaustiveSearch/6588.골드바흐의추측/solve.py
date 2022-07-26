import sys
input = sys.stdin.readline

def find_primes(n):
    sieve = [i for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] != 0:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(3, n + 1) if sieve[i] != 0 and sieve[i] % 2 == 1]

def solve(n, primes):
    c, d = 0, 0
    for i in range(len(primes)):
        a = n - primes[i]
        if a < 0: break
        if a in primes:
            b = n - a
            if b in primes:
                if b - a > d - a:
                    c, d = a, b
    print(f"{n} = {c} + {d}")

primes = find_primes(10000)
while True:
    n = int(input())
    if n == 0: break
    solve(n, primes)