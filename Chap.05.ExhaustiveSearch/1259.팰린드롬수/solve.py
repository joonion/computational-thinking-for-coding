def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
    
while True:
    n = int(input())
    if n == 0:
        break
    print("yes" if is_palindrome(n) else "no")
