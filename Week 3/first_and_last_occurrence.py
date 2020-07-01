s = input()
f_index = s.find('f')
if f_index == -1:
    print()
elif s[f_index + 1:].find('f') != -1:
    print(f_index, s.rfind('f'))
else:
    print(f_index)
