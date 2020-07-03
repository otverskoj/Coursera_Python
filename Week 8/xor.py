print(*map(lambda tpl: tpl[0] ^ tpl[1], zip(
    map(int, input().split()), map(int, input().split()))))
