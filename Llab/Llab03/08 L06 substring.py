'''
[substring] สตริงย่อย
สตริงย่อย คือ ส่วนหนึ่งของคำ หรือ ประโยค เช่น “aur” เป็นสตริงย่อยของ “restaurant” และ “for” เป็นสตริงย่อยของ “transformation”

จงเขียนโปรแกรมที่รับประโยคและสตริงย่อย จากนั้นแสดงตำแหน่งของสตริงย่อย หากไม่มีให้แสดง Not found และหากมีสตริงย่อยที่ซ้อนกันอยู่ ให้เลือกแสดงตามลำดับที่พบจากหน้าไปหลัง รับประกันว่าสตริงย่อยจะมีความยาวไม่เกินความยาวของประโยค

Example1
Text: Hey jude Don’t make it bad
Substring: ude
Hey j[ude] Don’t make it bad

Example2
Text: abcdeabc
Substring: abc
[abc]de[abc]
Example3

Text: you called me up again tonight
Substring: I
Not found
Example4

Text: ababababababababab
Substring: aba
[aba]b[aba]b[aba]b[aba]bab
'''

text = input("Text: ")
substring = input("Substring: ")

positions = []
start = 0

while True:
    pos = text.find(substring, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

if not positions:
    print("Not found")
else:
    selected_positions = []
    used = [False] * len(text)
    
    for pos in positions:
        if not any(used[pos:pos + len(substring)]):
            selected_positions.append(pos)
            for i in range(pos, pos + len(substring)):
                used[i] = True
    
    result = ""
    last_end = 0
    
    for pos in selected_positions:
        result += text[last_end:pos]
        result += "[" + text[pos:pos + len(substring)] + "]"
        last_end = pos + len(substring)
    
    result += text[last_end:]
    print(result)