x, y = int(input()), int(input())
days = 1
while x < y:
    x += x / 10
    days += 1
print(days)
