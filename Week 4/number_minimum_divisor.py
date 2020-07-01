def min_divisor(n):
    max_div = n ** 0.5
    d = 2
    while d <= max_div:
        if n % d == 0:
            return d
        else:
            d += 1
    else:
        return n


print(min_divisor(int(input())))
