def devision(a, b):
    try:
        return f"The result of devision is {(a / b):.2f}"
    except ZeroDivisionError as err:
        return f"Error: {err}"

arg1 = int(input("Enter the first number: "))
arg2 = int(input("Enter the second number: "))

print(devision(arg1, arg2))