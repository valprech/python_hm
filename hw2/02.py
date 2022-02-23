count = int(input("Enter the exect number of items: "))
my_list = []
i = 1
while count > 0:
    el = input(f"Enter number {i} item value: ")
    my_list.append(el)
    i = i + 1
    count = count - 1

print(my_list)

for i in range(1, len(my_list), 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]

print(my_list)