def seqsearch(x, S):
    for i in range(len(S)):
        if x == S[i]:
            return i
    return -1

from random import sample, randint
S = sample(range(1, 10), k = 5)
x = randint(1, 10)
p = seqsearch(x, S)
print(S)
print(f"x = {x}: pos = {p}.")