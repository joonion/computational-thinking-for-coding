def binsearch(x, S, low, high):
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid - 1
        else: # x > S[mid]
            low = mid + 1
    return -1

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    S = sorted(A)
    for i in range(M):
        j = binsearch(B[i], S, 0, len(S) - 1)
        print(0 if j < 0 else 1)
    