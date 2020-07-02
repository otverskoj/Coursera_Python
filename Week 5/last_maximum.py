num_list = list(map(int, input().split()))
curr_max = num_list[0]
curr_index = 0
for i in range(1, len(num_list)):
    if num_list[i] > curr_max:
        curr_max = num_list[i]
        curr_index = i
    elif num_list[i] == curr_max and i != curr_index:
        curr_index = i
print(curr_max, curr_index)
