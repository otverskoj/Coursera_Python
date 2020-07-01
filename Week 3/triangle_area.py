from math import sqrt

a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
area = sqrt(p * (p - a) * (p - b) * (p - c))
print(area)
