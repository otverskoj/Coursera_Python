s, n = tuple(map(int, input().split()))
users_data = []
for i in range(n):
    users_data.append(int(input()))
users_data.sort()
data_sum, counter = 0, 0
for data in users_data:
    curr_sum = data_sum + data
    if curr_sum < s:
        data_sum += data
        counter += 1
    else:
        break
print(counter)
