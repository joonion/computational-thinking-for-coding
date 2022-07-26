def is_prime(n):
    if n < 2:
        return False
    else:
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                return False
        return True

def solve(m, n):
    S, s = 0, 10 ** 4
    for k in range(m, n + 1):
        if is_prime(k):
            S += k
            s = min(s, k)
    if s < 10 ** 4:
        print(S)
    print(-1 if s == 10 ** 4 else s)
    
M = int(input())
N = int(input())
solve(M, N)
