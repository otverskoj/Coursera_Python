cow_number = int(input())
if 11 <= cow_number % 100 <= 19:
    print(cow_number, "korov", sep=' ')
elif cow_number % 10 == 1:
    print(cow_number, "korova", sep=' ')
elif 2 <= cow_number % 10 <= 4:
    print(cow_number, "korovy", sep=' ')
else:
    print(cow_number, "korov", sep=' ')
# korova: 1,
# korovy: 2,3,4,
# korov: 5,6,7,8,9,0
