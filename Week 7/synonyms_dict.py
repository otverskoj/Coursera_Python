n = int(input())
my_dict = dict()
for i in range(n):
    user_input = input().split()
    my_dict[user_input[0]] = user_input[1]
    my_dict[user_input[1]] = user_input[0]
print(my_dict[input()])
