'''
Find top K occurrences in a text
โดยทั่วไปแล้ว เราจะแยกคำในข้อความเท็กซ์ภาษาอังกฤษโดยใช้ช่องว่าง หรือตัวอักษรขึ้นบรรทัดใหม่

จงเขียนโปรแกรมที่รับข้อความเท๊กซ์แบบมัลติไลน์จากผู้ใช้งาน และค่าตัวเลข K แล้วโปรแกรมจะทำการวิเคราะห์ข้อความเท็กซ์นั้นเพื่อนับจำนวนการปรากฏคำ (number of word occurences) ทั้งหมด และพิมพ์เฉพาะคำที่ปรากฏมากสุดใน K ลำดับแรก (top K occurrences) ดังตัวอย่าง

ตัวอย่างการทำงาน 1
Parse a long paragraph (or text) below, following an ENTER as needed:
When the night has come
And the land is dark
And the moon is the only light we'll see
No I won't be afraid
Oh, I won't be afraid
Just as long as you stand, stand by me
So darling, darling
Stand by me, oh stand by me
Oh stand, stand by me
Stand by me
If the sky that we look upon
Should tumble and fall
Or the mountain should crumble to the sea
I won't cry, I won't cry
No, I won't shed a tear
Just as long as you stand, stand by me
And darling, darling
Stand by me, oh stand by me
Oh stand now, stand by me
Stand by me
Darling, darling
Stand by me, oh stand by me
Oh stand now, stand by me, stand by me
Whenever you're in trouble won't you stand by me
Oh stand by me, oh won't you stand now, stand
Stand by me
Top K rank: 5
stand: 21
by: 17
me: 12
oh: 8
the: 7, won't: 7

ตัวอย่างการทำงาน 2
Parse a long paragraph (or text) below, following an ENTER as needed:
a a b b c c d e f g g a h h b c x x x x
Top K rank: 3
x: 4
a: 3, b: 3, c: 3
g: 2, h: 2

ตัวอย่างการทำงาน 3
ในกรณีที่ค่า K มีค่ามากกว่าจำนวนลำดับของคำที่ปรากฏ ก็ให้พิมพ์เฉพาะผลลัพธ์คำเหล่านั้น

Parse a long paragraph (or text) below, following an ENTER as needed:
a b c c d d d e e d c
Top K rank: 5
d: 4
c: 3
e: 2
a: 1, b: 1

ตัวอย่างการทำงาน 4
Parse a long paragraph (or text) below, following an ENTER as needed:
I hope life treats you kind
And I hope you have all you've dreamed of
And I wish you joy and happiness
But above all this, I wish you love
And I will always love you
I will always love you
I will always love you
I will always love you
I will always love you
I, I will always love you
Top K rank: 4
i: 10, you: 10
love: 7
will: 6, always: 6
and: 4


[hide line #]
def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + ' '
    return text

### ให้เรียกใช้ฟังชัน getMultilinesInput() นี้ตอนเดฟได้เลย
#print("Parse a long paragraph (or text) below, following an ENTER as needed:")
#ss = getMultilinesInput()
#k = int(input("Top K rank: "))
หมายเหตุ
'i,' not the same as 'i'
ถ้าพบการใช้คำสั่ง import จะตัดคะแนนที่ทำได้ในข้อนี้ -70%
'''


def getMultilinesInput():
    x = ""
    while True:
        y = input()
        if not y:
            break
        x += y + ' '
    return x

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
x = getMultilinesInput()

x = x.lower().split()

k = int(input("Top K rank: "))

__ = {}
for i, j in enumerate(x):
    if j not in __:
        __[j] = i

y = {}
for i in x:
    y[i] = y.get(i, 0) + 1

x = sorted(y.items(), key=lambda _: (-_[1], __[_[0]]))

i = 0
j = 0

while j < k and i < len(x):
    _ = x[i][1]
    __ = []
    
    while i < len(x) and x[i][1] == _:
        __.append(x[i][0])
        i += 1
    
    print(", ".join(f"{y}: {_}" for y in __))
    j += 1