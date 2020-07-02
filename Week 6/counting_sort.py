def count_sort(lst):
    counters = [0 for i in range(101)]
    for elem in lst:
        counters[elem] += 1
    tmp_lst = []
    for i in range(101):
        for j in range(counters[i]):
            tmp_lst.append(i)
    return tmp_lst


num_lst = list(map(int, input().split()))
print(*count_sort(num_lst))
