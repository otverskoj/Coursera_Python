n = int(input())
participants = []
for i in range(n):
    participant = input().split()
    participants.append((int(participant[1]), participant[0]))
participants.sort(reverse=True)
for i in range(len(participants)):
    print(participants[i][1])
