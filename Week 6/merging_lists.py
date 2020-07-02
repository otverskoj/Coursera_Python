def merge(A, B):
    num_list = []
    i, j = 0, 0
    while i < len(A) or j < len(B):
        curr_min = min(A[i], B[j])
        if curr_min == A[i]:
            if i == len(A) - 1:
                num_list.append(curr_min)
                for elem in num_list_2[j:]:
                    num_list.append(elem)
                return num_list
            else:
                i += 1
        elif curr_min == B[j]:
            if j == len(B) - 1:
                num_list.append(curr_min)
                for elem in num_list_1[i:]:
                    num_list.append(elem)
                return num_list
            else:
                j += 1
        num_list.append(curr_min)
    num_list.append(max(A[-1], B[-1]))
    return num_list


num_list_1 = list(map(int, input().split()))
num_list_2 = list(map(int, input().split()))
ans = merge(num_list_1, num_list_2)
print(' '.join(map(str, ans)))
