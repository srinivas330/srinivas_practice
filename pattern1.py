# Number of lines in the pattern
n = 4

# Outer loop for each line
for i in range(1, n + 1):
    # Inner loop to print digits
    for j in range(i):
        print(i, end='')
    # Move to the next line after printing digits for the current line
    print()
