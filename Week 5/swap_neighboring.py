num_list = list(map(int, input().split()))
n = len(num_list)
for i in range(1, n, 2):
    if i == n - 1 and n % 2 != 0:
        break
    num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]
print(' '.join(map(str, num_list)))
