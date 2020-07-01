def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        d_max = n ** 0.5
        d = 3
        while d <= d_max:
            if n % d == 0:
                return False
            else:
                d += 2
        else:
            return True


if is_prime(int(input())):
    print("YES")
else:
    print("NO")
