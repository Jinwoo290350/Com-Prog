'''
Pairs of complete strings in two sets
Two strings are said to be complete if on concatenation, they contain all the 26 English alphabets. For example, “abcdefghi” and “jklmnopqrstuvwxyz” are complete as they together have all characters from ‘a’ to ‘z’. We are given two sets of sizes n and m respectively and we need to find the number of pairs that are complete on concatenating each string from set 1 to each string from set 2.

ตัวอย่างการทำงาน 1
String set1: ["abcdefgh", "geeksforgeeks", "lmnopqrst", "abc"]
String set2: ["ijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]
Output: 5
The total complete pairs that are forming are:
 abcdefghijklmnopqrstuvwxyz
 abcdefghabcdefghijklmnopqrstuvwxyz
 geeksforgeeksabcdefghijklmnopqrstuvwxyz
 lmnopqrstabcdefghijklmnopqrstuvwxyz
 abcabcdefghijklmnopqrstuvwxyz
ตัวอย่างการทำงาน 2
String set1: ["Twostringsaresaidtobe", "completeifonconcatenation"]
String set2: ["abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyz"]
Output: 2
The total complete pairs that are forming are:
 Twostringsaresaidtobeabcdefghijklmnopqrstuvwxyz
 completeifonconcatenationabcdefghijklmnopqrstuvwxyz
หมายเหตุ: ไม่อนุญาติให้ใช้โครงสร้างข้อมูลไพท่อนเซต และคำสั่ง import ถ้าตรวจพบ จะถูกหักคะแนน -70%
'''

line1 = input("String set1: ").strip()
line2 = input("String set2: ").strip()

set1 = eval(line1)
set2 = eval(line2)

count = 0
pairs = []
for s1 in set1:
    for s2 in set2:
        combined = s1 + s2
        chars = [False] * 26
        for c in combined.lower():
            if 'a' <= c <= 'z':
                chars[ord(c) - ord('a')] = True
        if all(chars):
            count += 1
            pairs.append(combined)

print(f"Output: {count}")
print("The total complete pairs that are forming are:")
for pair in pairs:
    print(f" {pair}")