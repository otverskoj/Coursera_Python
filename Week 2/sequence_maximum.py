n = int(input())
now_max = n
while n != 0:
    n = int(input())
    if now_max < n:
        now_max = n
print(now_max)
