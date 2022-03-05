def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    return sum(my_list)


a, b, c = int(input("Enter the first number: ")), int(input("Enter the second number: ")), int(
    input("Enter the third number: "))

print(my_func(a, b, c))
