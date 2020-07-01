def my_sum(a, b):
    if a == 0:
        return b
    else:
        return my_sum(a - 1, b + 1)


print(my_sum(int(input()), int(input())))
