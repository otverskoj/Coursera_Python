n1 = int(input())
n2 = int(input())
curr_max = n1 if n1 > n2 else n2
sec_max = n2 if n2 < n1 else n1
# если вторым элементом будет 0, то надо завершить работу (не заходить в цикл)
n = n1 * n2
while n != 0:
    n = int(input())
    if n >= curr_max:
        sec_max = curr_max
        curr_max = n
    elif n < curr_max and n > sec_max:
        sec_max = n

print(sec_max)
