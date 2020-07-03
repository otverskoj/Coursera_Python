n = int(input())
questions_list = []
user_input = input()
while user_input != 'HELP':
    if user_input != 'YES' and user_input != 'NO':
        questions_list.append((list(map(int, user_input.split())), input()))
    user_input = input()
numbers = set([i for i in range(1, n + 1)])
for tpl in questions_list:
    tpl_set = set(tpl[0])
    if tpl[1] == 'NO':
        numbers -= tpl_set
    elif tpl[1] == 'YES':
        numbers &= tpl_set
print(*sorted(numbers))
