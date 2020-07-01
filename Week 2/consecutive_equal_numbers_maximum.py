n = int(input())
curr_n = n
max_cons = 1
curr_max_cons = max_cons
while n != 0:
    n = int(input())
    if n == curr_n:
        max_cons += 1
        if max_cons > curr_max_cons:
            curr_max_cons = max_cons
    else:
        curr_n = n
        max_cons = 1
print(curr_max_cons)
