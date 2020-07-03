fin = open('input.txt')
words_number = dict()
ans = []
for line in fin:
    line = line.split()
    for word in line:
        word = word.strip()
        if word not in words_number:
            words_number[word] = 0
            ans.append(0)
        else:
            words_number[word] += 1
            ans.append(words_number[word])
print(*ans)
