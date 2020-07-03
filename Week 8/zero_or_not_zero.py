print(not all(map(lambda x: x > 0, map(
    int, open('input.txt').readlines()[1:]))))
