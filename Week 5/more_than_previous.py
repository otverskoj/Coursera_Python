num_list = list(map(int, input().split()))
for i in range(1, len(num_list)):
    if num_list[i - 1] < num_list[i]:
        print(num_list[i], end=' ')
