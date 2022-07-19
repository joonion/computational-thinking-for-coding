squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

M1 = [(i, j) for j in range(3) for i in range(2)]
print(M1)

M2 = [[(i, j) for j in range(3)] for i in range(2)]
print(M2)

a = [i for i in range(1, 11)]
b = [j for j in a if a[-1] % j == 0]
print(b)

