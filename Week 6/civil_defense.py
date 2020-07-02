n = int(input())
vil_list = list(map(int, input().split()))
villages = []
for i in range(n):
    villages.append((vil_list[i], i))
villages.sort()
m = int(input())
shelt_list = list(map(int, input().split()))
shelters = []
for i in range(m):
    shelters.append((shelt_list[i], i))
shelters.sort()

ans = [0 for i in range(n)]
start = 0
for i in range(n):
    min_dist = 10e10
    shelter = start
    for j in range(start, m):
        curr_min_dist = abs(villages[i][0] - shelters[j][0])
        if curr_min_dist < min_dist:
            min_dist = curr_min_dist
            shelter = shelters[j][1]
            start = j
        else:
            break
    ans[villages[i][1]] = shelter + 1
print(*ans)
