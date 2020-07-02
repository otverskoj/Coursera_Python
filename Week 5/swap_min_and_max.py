num_list = list(map(int, input().split()))
list_min = 10000
list_max = -10000
index_min, index_max = 0, 0
for i in range(len(num_list)):
    curr_min, curr_max = num_list[i], num_list[i]
    if curr_min < list_min:
        list_min = curr_min
    if curr_max > list_max:
        list_max = curr_max
index_min = num_list.index(list_min)
index_max = num_list.index(list_max)
num_list[index_min], num_list[index_max] = \
    num_list[index_max], num_list[index_min]
print(' '.join(map(str, num_list)))
