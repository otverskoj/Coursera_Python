n = int(input())
series_sum = 0
i = 1
while i <= n:
    series_sum += 1 / (i ** 2)
    i += 1
print(series_sum)
