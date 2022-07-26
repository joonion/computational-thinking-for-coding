def binsearch(x, S, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return binsearch(x, S, low, mid - 1)
        else: # x > S[mid]
            return binsearch(x, S, mid + 1, high)

from random import sample, randint
S = sample(range(1, 10), k = 5)
x = randint(1, 10)
S.sort()
p = binsearch(x, S, 0, len(S) - 1)
print(S)
print(f"x = {x}: pos = {p}.")