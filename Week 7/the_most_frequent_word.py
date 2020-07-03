fin = open('input.txt')
my_dict = dict()
for line in fin:
    line = line.split()
    for word in line:
        my_dict[word] = my_dict.get(word, 0) + 1
print(max(sorted(my_dict), key=my_dict.get))
