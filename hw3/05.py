def my_func():
    sum = 0

    while True:
        my_list = input("Enter the list of numbers devided by space: ").split()

        for i in my_list:
            if i.lower() == "q":
                return sum
            else:
                try:
                    sum += int(i)
                except ValueError:
                    print("Enter 'q' to exit: ")
        print(f'Total sum is {sum}')


print(my_func())
