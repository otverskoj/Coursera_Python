fin = open('input.txt')
my_dict = dict()
for line in fin:
    line = line.split()
    for word in line:
        my_dict[word] = my_dict.get(word, 0) + 1
ans = []
for elem in sorted(my_dict):
    ans.append((my_dict[elem], elem))
ans = sorted(ans, key=lambda t: t[0], reverse=True)
for tpl in ans:
    print(tpl[1])
