#variant 1
month = int(input("Enter the month number to find the season: "))
seasons = {'winter': (12, 1, 2), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'fall': (9, 10, 11)}

for k, v in seasons.items():
    if month in v:
        print(f"The number {month} month is {k}")

#variant 2
month = int(input("Enter the month number to find the season: "))
seasons = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
print(f"The month number {month} is {seasons[month - 1]}")