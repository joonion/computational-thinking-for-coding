def solve(n, k):
    cnt = 0
    for d in range(1, n + 1):
        if n % d == 0:
            cnt += 1
        if cnt == k:
            return d
    return 0

N, K = map(int, input().split())
print(solve(N, K))