def solve(n, low, high):
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 < n:
            low = mid + 1
        else: # mid ** 2 > n
            high = mid - 1
    return low

n = int(input())
print(solve(n, 0, n))