A = int(input())
B = int(input())
C = list(map(int, str(B)))
for c in C[::-1]:
    print(A * c)
print(A * B)