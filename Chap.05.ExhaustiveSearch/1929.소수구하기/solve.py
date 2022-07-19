def is_prime(n):
    if n < 2:
        return False
    else:
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                return False
        return True

def solve(m, n):
    for k in range(m, n + 1):
        if is_prime(k):
            print(k)

M, N = map(int, input().split())
solve(M, N)
