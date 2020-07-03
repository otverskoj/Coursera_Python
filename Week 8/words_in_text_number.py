from functools import reduce
print(len(reduce(lambda s1, s2: s1 | s2, map(
    set, map(lambda lst: lst.split(),
             open('input.txt').readlines())))))
