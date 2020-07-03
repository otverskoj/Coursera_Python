ang = []
union = set()
all1 = set()
for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)}
    all1.update(a)
    if i == 1:
        union.update(a)
    else:
        union &= a
print(len(union))
print('\n'.join(sorted(union)))
print(len(all1))
print('\n'.join(sorted(all1)))
