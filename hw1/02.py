time = int(input('Enter time in seconds: '))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

print('{:0>2}:{:0>2}:{:0>2}'.format(hours, minutes, seconds))