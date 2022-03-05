def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    res = 1
    for i in range(0, (y * -1)):
        res = res / x
    return res


arg1 = float(input("Enter the positive number: "))
arg2 = int(input("Enter the negative degree of power: "))

print(my_func(arg1, arg2))
print(my_func_2(arg1, arg2))
