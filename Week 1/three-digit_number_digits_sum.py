number = int(input())
digits_sum = int(number / 100) + int(number / 10) % 10 + number % 10
print(digits_sum)
