n = int(input())
i = 1
while i <= n:
    for j in range(1, i + 1):
        print(j, end='')
    print()
    i += 1
