n = int(input())
curr_max = n
max_elems_num = 1
while n != 0:
    n = int(input())
    if n > curr_max:
        curr_max = n
        max_elems_num = 1
    elif n == curr_max:
        max_elems_num += 1
print(max_elems_num)
