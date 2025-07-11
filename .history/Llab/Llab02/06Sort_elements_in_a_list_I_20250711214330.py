x = input("Enter list of tuple: ").split()
for i in range(len(x)):
    x[i] = tuple(map(int, x[i].split(',')))
    
