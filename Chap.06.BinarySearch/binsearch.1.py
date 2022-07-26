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

from random import sample, randint
S = sample(range(1, 10), k = 5)
x = randint(1, 10)
S.sort()
p = binsearch(x, S, 0, len(S) - 1)
print(S)
print(f"x = {x}: pos = {p}.")