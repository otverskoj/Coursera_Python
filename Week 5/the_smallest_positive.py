num_list = list(map(int, input().split()))
curr_positive_min = max(num_list)
for num in num_list:
    if num > 0 and num < curr_positive_min:
        curr_positive_min = num
print(curr_positive_min)
