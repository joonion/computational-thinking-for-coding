def solve(n):
    T = [1, 1]
    while T[-1] < n:
        T.append(T[-1] * len(T))
        print(T)
    return False

n = int(input())
print("YES" if solve(n) else "No")
