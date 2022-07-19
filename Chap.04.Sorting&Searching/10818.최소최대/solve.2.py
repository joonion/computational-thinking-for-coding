def solve(n, A):
    smallest, largest = 10**6, -10**6
    for i in range(n):
        smallest = min(smallest, A[i])
        largest = max(largest, A[i])
    return smallest, largest
        
N = int(input())
A = list(map(int, input().split()))
s, l = solve(N, A)
print(s, l)