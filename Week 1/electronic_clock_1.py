N = int(input())
N = N % 1440
hours = int(N / 60)
minutes = N - (hours * 60)
print(hours, minutes, sep=' ')
