'''
[mine_sweeper] แผนที่ระเบิด
Minesweeper เป็นเกมหาระเบิดในทุ่งระเบิดซึ่งเป็นเมทริกซ์ขนาด m x n โดยช่องที่มีระเบิดจะระบุด้วย ‘X’ และช่องที่ไม่มีระเบิดจะบอกจำนวนระเบิดที่อยู่รอบตัว (ซึ่งมีค่าไม่เกิน 8 ลูก) กำหนดการเรียกชื่อพิกัดดังนี้

สำหรับเมทริกซ์ขนาด 4 x 4

|(0,0)|(1,0)|(2,0)|(3,0)|
|(0,1)|(1,1)|(2,1)|(3,1)|
|(0,2)|(1,2)|(2,2)|(3,2)|
|(0,3)|(1,3)|(2,3)|(3,3)|
จงเขียนโปรแกรมที่รับขนาดตาราง จำนวนระเบิด และพิกัดของระเบิด และแสดงแผนที่ระเบิด
Example1
Grid Size: 4 4
Number of mine(s): 3
Mine#1: 0 0
Mine#2: 1 2
Mine#3: 2 3
X 1 0 0
2 2 1 0
1 X 2 1
1 2 X 1
Example2
Grid Size: 3 3
Number of mine(s): 4
Mine#1: 0 0
Mine#2: 1 2
Mine#3: 2 2
Mine#4: 0 2
X 1 0
3 4 2
X X X
Note: จาก Sample Output 1 ในพิกัด (1,0) มีระเบิดที่อยู่รอบตัว 1 ลูก คือที่พิกัด (0,0) และ
                                         ในพิกัด (1,1) มีระเบิดที่อยู่รอบตัว 2 ลูก คือที่พิกัด (0,0) และ พิกัด (1,2)

Example3
Grid Size: 3 4
Number of mine(s): 4
Mine#1: 0 0
Mine#2: 1 2
Mine#3: 2 2
Mine#4: 2 0
X 2 X 
2 4 3 
1 X X 
1 2 2 
'''

size = input("Grid Size: ").split()
mine = int(input("Number of mine(s): "))
size = [int(x) for x in size]

mine_positions = []
for i in range(mine):
    x, y = input(f"Mine#{i+1}: ").split()
    x = int(x)
    y = int(y)
    mine_positions.append((x, y))
    
def create_grid(size):
    grid = []
    for i in range(size[1]):
        row = []
        for j in range(size[0]):
            row.append(0)
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))

def place_mines(grid, size, mine_positions):
    for pos in mine_positions:
        x, y = pos
        grid[y][x] = 'X'
        for i in range(max(0, y-1), min(size[1], y+2)):
            for j in range(max(0, x-1), min(size[0], x+2)):
                if grid[i][j] != 'X':
                    grid[i][j] += 1
    
grid = create_grid(size)
place_mines(grid, size, mine_positions)
print_grid(grid)