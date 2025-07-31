row = int(input("Enter Rook's row position: "))
col = int(input("Enter Rook's column position: "))

board = [[' ' for _ in range(8)] for _ in range(8)]

board[row][col] = 'R'

for c in range(8):
    if c != col:
        board[row][c] = 'x'

for r in range(8):
    if r != row:
        board[r][col] = 'x'

for r in range(8):
    print("-----------------")
    for c in range(8):
        print("|" + board[r][c], end="")
    print("|")
print("-----------------")