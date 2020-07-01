def seq_sum():
    n = int(input())
    if n != 0:
        return n + seq_sum()
    return 0


print(seq_sum())
