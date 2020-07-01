def reduce_fraction(n, m):
    p1 = max(n, m)
    p2 = min(n, m)
    if p1 == p2 and p1 * p2 != 0:
        return 1, 1
    else:
        p = p1 % p2
        while p > 0:
            p1 = p2
            p2 = p
            p = p1 % p2
        return n // p2, m // p2


print(*reduce_fraction(int(input()), int(input())))
