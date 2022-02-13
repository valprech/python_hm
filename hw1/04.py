number = int(input('Enter number: '))
max_number = 0

while number > 0:
    excess = number % 10
    if excess > max_number:
        max_number = excess
    number = number // 10

print(max_number)