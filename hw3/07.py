def int_func(str):
    str = str.capitalize()
    return str


def upper_func():
    sent = input("Enter the sentence you like in lowercase form: ").split()
    for i in range(len(sent)):
        sent[i] = int_func(sent[i])
    return " ".join(sent)


print(upper_func())
