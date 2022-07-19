def sumofdigits(n):
    s, t = 0, n
    while t > 0:
        s += t % 10
        t = t // 10
    return s

def solve(n):
    for m in range(1, n + 1):
        if n == m + sumofdigits(m):
            return m
    return 0

N = int(input())
print(solve(N))