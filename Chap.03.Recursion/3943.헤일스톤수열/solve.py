import sys
input = sys.stdin.readline

def solve(n):
    largest = n
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        largest = max(largest, n)
    return largest

for _ in range(int(input())):
    print(solve(int(input())))