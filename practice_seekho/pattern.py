num = 8
for i in range(1, num + 1):
    # Inner loop for each star in the line
    for j in range(i):
        print('*', end='')
    # Move to the next line after printing stars
    print()
