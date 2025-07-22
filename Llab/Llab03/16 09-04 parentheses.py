'''
Parentheses ครบคู่ไหมนะ
ให้นิสิตพัฒนาโปรแกรมเพื่อหาว่าสตริงทีประกอบไปด้วยวงเล็บที่รับเข้ามามีวงเล็บเปิดปิดครบคู่หรือไม่ โดยวงเล็บดังกล่าวต้องเรียงให้ถูกคู่และถูกลำดับด้วย.

หมายเหตุ ตรวจพบคำสั่ง import หัก 70% ของคะแนนที่ได้รับ

example
input: ()[]{}
valid parentheses
example
input: {[()]}
valid parentheses
example
input: ([)]
invalid parentheses
example
input: (
invalid parentheses
example
input: while ("{{" in x or "[]" in x or "("  in x or " " in x): pass
valid parentheses
'''

dic = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

parentheses = input("input: ").strip()

cleaned = ''
inside_quotes = False

for char in parentheses:
    if char == '"':
        inside_quotes = not inside_quotes
        cleaned += char
    elif inside_quotes and (char in dic or char in dic.values()):
        continue
    else:
        cleaned += char

stack = []

for char in cleaned:
    if char in dic:
        stack.append(char)
    elif char in dic.values():
        if not stack or dic[stack[-1]] != char:
            print("invalid parentheses")
            exit()
        stack.pop()

if not stack:
    print("valid parentheses")
else:
    print("invalid parentheses")