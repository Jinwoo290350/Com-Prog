'''
Word chain โซ่คำ
โซ่คำ คือลำดับของคำที่มีจำนวนอักขระเท่ากันและแต่ละคำที่มีลำดับติดกันจะต้องมีตำแหน่งที่มีตัวอักขระต่างกันไม่เกินสองตำแหน่ง เช่น
    HEAD และ HEAP จะต่างกันตำแหน่งเดียว คือ D และ P ในตำแหน่งตัวอักขระที่ 4 ของคำ
ตัวอย่างที่ไม่เป็นโซ่คำ เช่น
    REAR และ BAER จะต่างกัน 3 ตำแหน่ง คือ ตำแหน่งที่ 1 (R กับ B) ตำแหน่งที่ 2 (E กับ A) และ ตำแหน่งที่ 3 (A กับ E)

ตัวอย่างของโซ่คำที่ต่อเนื่อง ได้แก่ HEAD HEAP LEAP TEAR REAR และ EGG EAG GAE GAP TAP TIN
ตัวอย่างของโซ่คำที่ขาด ได้แก่ LEAP TEAR REAR BAER BAET BEEP ซึ่งจะขาดที่คำว่า RAER และ BAER ได้เป็นโซ่ 2 เส้น

จงเขียนโปรแกรมเพื่อแสดงว่ามีโซ่คำสั้นทั้งหมดกี่เส้นในข้อความ และ เส้นที่ยาวที่สุดยาวเท่าไร รับประกันว่าแต่ละคำจะมีจำนวนตัวอักษรเท่ากัน และ ประกอบด้วยตัวอักษรภาษาอังกฤษพิมพ์ใหญ่ ('A' ถึง 'Z') เท่านั้น

Example 1
Text: HEAD HEAP LEAP TEAR REAR BAER BAET BEEP JEEP JOIP JEIP AEIO
2 Chain(s). Maximum length is 7 word(s).
Note: สามารถแบ่งได้ 2 เส้น ดังนี้
HEAD HEAP LEAP TEAR REAR มีความยาวเป็น 5 คำ
BAER BAET BEEP JEEP JOIP JEIP AEIO มีความยาวเป็น 7 คำ
Example 2
Text: SUN TON BOW GOD LOT KID FAX BAT FAT CAR EAT FEE SEA MAP DRY SPY TAP
7 Chain(s). Maximum length is 5 word(s).
Note: สามารถแบ่งได้ 2 เส้น ดังนี้
SUN TON BOW GOD LOT มีความยาวเป็น 5 คำ
KID มีความยาวเป็น 1 คำ
FAX BAT FAT CAR EAT มีความยาวเป็น 5 คำ
FEE SEA มีความยาวเป็น 2 คำ
MAP มีความยาวเป็น 1 คำ
DRY SPY มีความยาวเป็น 2 คำ
TAP มีความยาวเป็น 1 คำ

[hide line #]

'''

def can_chain(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
            if diff > 2:
                return False
    return True

text = input("Text: ")
words = text.split()

chains = []
current_chain = [words[0]]

for i in range(1, len(words)):
    if can_chain(current_chain[-1], words[i]):
        current_chain.append(words[i])
    else:
        chains.append(current_chain)
        current_chain = [words[i]]

chains.append(current_chain)

num_chains = len(chains)
max_length = max(len(chain) for chain in chains)

print(f"{num_chains} Chain(s). Maximum length is {max_length} word(s).")