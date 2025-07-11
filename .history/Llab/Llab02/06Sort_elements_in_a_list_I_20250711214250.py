x = input("Enter list of tuple: ").split()
x = [tuple(map(int, i.split(','))) for i in x]
x.sort(key=lambda i: (i[0], i[1]))
for i in x:
    print(i)