def divisor(n):
    div = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(list(div))

N, K = map(int, input().split())
D = divisor(N)
print(D[K - 1] if K <= len(D) else 0)