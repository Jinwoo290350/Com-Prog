'''
[Longest Word] ค้นหาคำที่ยาวที่สุดในแต่ละตัวอักษร
คุณได้รับมอบหมายให้เขียนโปรแกรมที่รับสตริงประโยคจากผู้ใช้ และค้นหาคำที่ยาวที่สุดสำหรับแต่ละตัวอักษรตัวแรกของคำนั้น โดยถ้ามีหลายคำที่ขึ้นต้นด้วยตัวอักษรเดียวกันและมีความยาวเท่ากัน ให้เลือกพิมพ์เฉพาะคำแรกที่พบ พิมพ์ผลลัพธ์ตามลำดับการพบตัวอักษรตัวแรกนั้นๆ

ตัวอย่างเช่น

Enter your sentence: Hello wonderful World
H: Hello
W: wonderful
กรณีพิเศษเมื่อมีทุกตัวอักษรและมีความยาวแตกต่างกัน:

Enter your sentence: apple banana cherry date fig grape Guava
A: apple
B: banana
C: cherry
D: date
F: fig
G: grape
'''

x = input("Enter your sentence: ").split()
words = {}

for i in x:
    if i[0].upper() not in words:
        words[i[0].upper()] = len(i)
    else:
        if len(i) > words[i[0].upper()]:
            words[i[0].upper()] = len(i)
                
for w in words:
    for i in x:
        if w == i[0].upper() and words[w] == len(i):
            print(f"{w}: {i}")
            break
