'''
Submitted on 17:01 24 Jul 2025 || Result: PASSED [PPPP] Explain results Copy to current
Returning vowels and consonants of a given string
Given a string input, find what character vowel(s) and consonant(s) appear in?

ตัวอย่างการทำงาน 1
Enter a string: Apple
Unique vowels:  ['a', 'e']
Unique consonants:  ['p', 'l']
ตัวอย่างการทำงาน 2
Enter a string: Apple Banana Carrot
Unique vowels:  ['a', 'e', 'o']
Unique consonants:  ['p', 'l', 'b', 'n', 'c', 'r', 't']
หมายเหตุ: ไม่อนุญาติให้ใช้โครงสร้างข้อมูลไพท่อนเซต และคำสั่ง import ถ้าตรวจพบ จะถูกหักคะแนน -70%
'''

x = input("Enter a string: ").split()
apha = ["a","e","i","o","u"]
con = []
vow = []
for j in x:
    for i in j:
        if i.isalpha():
            if i.lower() not in apha and i.lower() not in con:
                con.append(i.lower())
            elif i.lower() not in vow and i.lower() in apha:
                vow.append(i.lower())
            
print(f"Unique vowels:  {vow}")
print(f"Unique consonants:  {con}")
