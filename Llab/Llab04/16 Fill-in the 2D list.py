n = int(input("Enter the number of rows or columns : "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print('%2d ' % (i + j - 1), end='')
    print()