def solve(n, m):
    return (m * (m + 1) - n * (n - 1)) // 2

N = int(input())
M = int(input())
print(solve(N, M))