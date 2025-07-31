direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))

matrix = []
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)

print("After flip:")
if direction == "V":
    for i in range(size - 1, -1, -1):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print()
elif direction == "H":
    for i in range(size):
        for j in range(size - 1, -1, -1):
            print(matrix[i][j], end=" ")
        print()