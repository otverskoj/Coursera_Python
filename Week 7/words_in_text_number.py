fin = open('input.txt', 'r', encoding='utf8')
unique_words = set()
for line in fin.readlines():
    for word in line.split():
        unique_words.add(word)
print(len(unique_words))
