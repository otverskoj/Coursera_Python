even_num = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n % 2 == 0:
        even_num += 1
print(even_num)
