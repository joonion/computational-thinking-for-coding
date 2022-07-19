fact = 1
n = 0
while fact <= 1000000000000000000:
    if n > 1:
        fact = n * fact
    print(n, fact)
    n += 1
