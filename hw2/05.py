el = int(input('Enter a number: '))
my_list = [7, 5, 3, 3, 2]

for k, v in enumerate(my_list):
    if v < el:
        my_list.insert(k, el)
        break
else:
    my_list.append(el)

print(my_list)
