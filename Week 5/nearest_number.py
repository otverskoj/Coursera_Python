size = int(input())
num_list = list(map(int, input().split()))
x = int(input())
min_diff = 2000
ans = num_list[0]
for num in num_list:
    curr_diff = abs(x - num)
    if curr_diff < min_diff:
        min_diff = curr_diff
        ans = num
print(ans)
