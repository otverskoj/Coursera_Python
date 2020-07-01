s = input()
first_occurr = s.find('h')
last_occurr = s.rfind('h')
print(s[:first_occurr] + s[last_occurr + 1:])
