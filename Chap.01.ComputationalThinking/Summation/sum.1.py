def solve(n, m):
    s = 0
    for i in range(n, m + 1):
        s = s + i
    return s

N = int(input())
M = int(input())
print(solve(N, M))