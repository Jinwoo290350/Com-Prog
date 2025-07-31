'''
modulo หารเอาเศษ
กำหนดจำนวนเต็ม A และ B เมื่อ A modulo B จะได้ผลลัพธ์เป็นเศษจากการหาร A ด้วย B เช่น 7,14,27,38 เมื่อ modulo ด้วย 3 จะได้ผลลัพธ์เป็น 1,2,0 และ 2 ตามลำดับ

ให้เขียนโปรแกรมรับจำนวนเต็ม N จำนวน จากนั้นทำการ modulo แต่ละจำนวนด้วย M

จากนั้นจะพบว่าผลลัพธ์ในการ modulo แต่ละครั้งอาจจะเท่ากันหรือไม่เท่ากันก็ได้ จึงให้หาว่า จากจำนวนทั้ง N จำนวนนั้น มีผลลัพท์ที่แตกต่างกันได้กี่แบบ

เช่น มีจำนวน คือ 5 6 7 8 9 ทำการ modulo ด้วย 3 ได้ผลคือ 2 0 1 2 0 จะพบว่ามีผลลัพท์ที่แตกต่างกันแค่ 3 แบบ คือ 0 1 2 จึงได้ 3 แบบเป็นคำตอบ

Example 1
N: 10
M: 42
Input number 1: 1
Input number 2: 2
Input number 3: 3
Input number 4: 4
Input number 5: 5
Input number 6: 6
Input number 7: 7
Input number 8: 8
Input number 9: 9
Input number 10: 10
10
Example 2
N: 10
M: 42
Input number 1: 39
Input number 2: 40
Input number 3: 41
Input number 4: 42
Input number 5: 43
Input number 6: 44
Input number 7: 82
Input number 8: 83
Input number 9: 84
Input number 10: 85
6
Example 3
N: 15
M: 10
Input number 1: 10
Input number 2: 20
Input number 3: 30
Input number 4: 40
Input number 5: 50
Input number 6: 60
Input number 7: 70
Input number 8: 80
Input number 9: 90
Input number 10: 100
Input number 11: 120
Input number 12: 130
Input number 13: 140
Input number 14: 1000
Input number 15: 10
1
Note: จาก Example 1 1%42 = 1, 2%42 = 2,..., 10%42 = 10 ดังนั้นจึงมีเศษทั้งหมด 10 รูปแบบ
         จาก Example 2 มีเศษจากการหารด้วย 42 ทั้งหมด 6 รูปแบบนั่นคือ 0(42,84), 1(43,85), 2(44), 39(39), 40(40,82), 41(41,83)



'''

n = int(input("N: "))
m = int(input("M: "))
numbers = []

for i in range(n):
    num = int(input(f"Input number {i+1}: "))
    numbers.append(num)
    
ans = []
answer = 0
for j in range(len(numbers)):
    space = numbers[j] % m
    if space not in ans:
        ans.append(space)
        answer +=1
print(answer)