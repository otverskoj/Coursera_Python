fin = open('input.txt', 'r', encoding='utf8')
participiants = [line.strip() for line in fin.readlines()]
participiants.sort()
for participiant in participiants:
    participiant = participiant.split()
    print(participiant[0], participiant[1], participiant[3])
