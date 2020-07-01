def seq_revers():
    n = int(input())
    if n != 0:
        seq_revers()
        print(n)
    else:
        print(n)


seq_revers()
