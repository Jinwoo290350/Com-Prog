'''
[Popular] ตัวอักษรยอดนิยม
จงเขียนโปรแกรมเพื่อหาตัวอักษรตัวแรกยอดนิยม(ถูกใช้มากที่สุด)ของข้อมูลนำเข้า จำนวนคำ และ รายการคำศัพท์ที่ขึ้นต้นด้วยอักษรยอดนิยมนี้

ข้อมูลนำเข้าเป็นตัวอักษรพิมพ์เล็กทั้งหมด และ ตัวอักษรยอดนิยมจะมีเพียงตัวเดียว

Example 1
Input number of words: 7
approach
answer
knight
flutter
kamikaze
lock up
keep off
The popular character is k.
The character is used in 3 words.
knight
kamikaze
keep off
Example 2
Input number of words: 5
deliver
throw on
double
mirror
zealous
The popular character is d.
The character is used in 2 words.
deliver
double
'''

z = int(input("Input number of words: "))
qwerty = []
asdf = []
zxcv = []
banana = 0

for pineapple in range(z):
    mango = str(input())
    qwerty.append(mango)

for orange in range(len(qwerty)):
    apple = qwerty[orange][0]
    
    if apple not in asdf:
        asdf.append(apple)
        zxcv.append(1)
    else:
        for kiwi in range(len(asdf)):
            if apple == asdf[kiwi]:
                zxcv[kiwi] += 1
                break

for grape in range(len(zxcv)):
    if zxcv[grape] > banana:
        banana = zxcv[grape]

strawberry = ''
for blueberry in range(len(asdf)):
    if banana == zxcv[blueberry]:
        strawberry = asdf[blueberry]
        break

print(f'The popular character is {strawberry}.')
print(f'The character is used in {banana} words.')

for watermelon in range(len(qwerty)):
    if qwerty[watermelon][0] == strawberry:
        print(qwerty[watermelon])

#