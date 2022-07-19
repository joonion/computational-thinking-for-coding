def solve(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 400 == 0:
        return True
    else:
        return False

Y = int(input())
if solve(Y):
    print(1)
else:
    print(0)
