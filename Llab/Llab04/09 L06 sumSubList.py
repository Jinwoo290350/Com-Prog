'''
รวมลิสย่อย [sumSubList]
จงเขียนโปรแกรมรับค่าชุดตัวเลขเพื่อนำไปบันทึกลง list

โดยโปรแกรมจะต้องสามารถตอบได้ว่าตั้งแต่ตัวเลขตำแหน่งที่ 
x
 ถึง 
y
 มีผลรวมเท่าไร

โดยที่ 
x
 และ 
y
 สามารถเป็นค่าติดลบได้

คือ 
−
1
 หมายถึงตำแหน่งสุดท้ายของ list

และ 
0
 หมายถึงตำแหน่งแรกของ list

โปรแกรมจะต้องรับค่า 
x
 และ 
y
 จนกว่า ตำแหน่งของ list ช่องที่ 
x
 อยู่ทางด้านขวาของ list ช่องที่ 
y
 แล้วโปรแกรมจึงหยุดการทำงาน

โปรแกรมนี้จะมีทั้งหมด 
k
 บรรทัด โดยที่ 
k
 เป็นจำนวนเต็มบวกคู่ใดๆ ในแต่ละบรรทัดประกอบด้วยข้อมูลนำเข้าและส่งออกดังนี้

ข้อมูลนำเข้า
บรรทัดที่ 1 : ชุดตัวเลขจำนวนเต็ม คั่นด้วยช่องว่าง

บรรทัดที่ 2,4,6...,
k
 : ตัวเลขจำนวนเต็ม 
x
 และ 
y

หาก ค่า 
x
 และ 
y
 ที่ใส่เข้าไปไม่อยู่ในช่วง 
−
l
e
n
(
l
i
s
t
)
≤
x
,
y
≤
l
e
n
(
l
i
s
t
)
−
1
 ให้แสดงว่า Bad Input และให้รับค่าใหม่

ข้อมูลส่งออก
บรรทัดที่ 3,5,7...,
k
−
1
 : ผลรวมเลขจำนวนเต็มของ list ตั้งแต่ช่องที่ 
x
 ถึงช่องที่ 
y
 จากบรรทัดบรรทัดที่ 2,4,6...,
k
−
2

Example 1
6 7 8 9 10
0 4
40
2 3
17
-5 -4
13
4 3
Example 2
1 2 3 4 5
0 0
1
0 4
15
-5 -1
15
-5 2
6
2 -1
12
4 0
Example 3
-10 -9 -8 -7 34
-5 -1
0
2 -1
19
-1 -3
Example 4
-10 -9 -8 -7 34
-6 -1
x Bad Input
0 5
y Bad Input
-6 5
x and y Bad Input
5 -6
x and y Bad Input
1 0
'''

numbers = list(map(int, input().split()))
n = len(numbers)

while True:
    x, y = map(int, input().split())
    
    x_valid = -n <= x <= n - 1
    y_valid = -n <= y <= n - 1
    
    if not x_valid and not y_valid:
        print("x and y Bad Input")
        continue
    elif not x_valid:
        print("x Bad Input")
        continue
    elif not y_valid:
        print("y Bad Input")
        continue
    
    if x < 0:
        x = n + x
    if y < 0:
        y = n + y
    
    if x > y:
        break
    
    result = sum(numbers[x:y+1])
    print(result)