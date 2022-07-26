def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n < 2:
        return False
    else:
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                return False
        return True

def solve(n):
    while True:
        if is_palindrome(n) and is_prime(n):
            return n
        n += 1

N = int(input())
print(solve(N))
