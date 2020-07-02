num_list = list(map(int, input().split()))
counter = 0
for i in num_list:
    if i > 0:
        counter += 1
print(counter)
