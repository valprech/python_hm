start = int(input('Enter the number of kilometers you ran during the first day: '))
goal = int(input('Enter the desired number of kilometers you want to run a day: '))

day = 1

while start < goal:
    day += 1
    start += start * .10
else:
    print(f'You will reach your goal on the {day}th day!')