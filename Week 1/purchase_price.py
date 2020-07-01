A = int(input())
B = int(input())
N = int(input())
rubles = A * N + int(B * N / 100)
pennies = B * N % 100
print(rubles, pennies, sep=' ')
