fin = open('input.txt', encoding='utf8')
text = fin.read().splitlines()
my_dict = dict()
voices_number = 0
for line in text:
    voices_number += 1
    line = line.strip()
    my_dict[line] = my_dict.get(line, 0) + 1
ans = []
for elem in my_dict:
    ans.append((my_dict[elem], elem))
ans.sort(reverse=True)
fout = open('output.txt', 'w', encoding='utf8')
if ans[0][0] / voices_number > 0.5:
    fout.write(ans[0][1])
else:
    fout.write(ans[0][1] + '\n')
    fout.write(ans[1][1])
fout.close()
