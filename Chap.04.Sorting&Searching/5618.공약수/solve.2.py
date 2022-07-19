def divisor(n):
    div = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(list(div))

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def solve(n, A):
    G = gcd(A[0], A[1])
    if N == 3:
        G = gcd(G, A[2])
    for d in divisor(G):
        print(d)

N = int(input())
A = list(map(int, input().split()))
solve(N, A)