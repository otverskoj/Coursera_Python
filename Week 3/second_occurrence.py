s = input()
first_f_index = s.find('f')
if first_f_index != -1:
    sec_f_index = s.find('f', first_f_index + 1)
    print(sec_f_index)
else:
    print(-2)
