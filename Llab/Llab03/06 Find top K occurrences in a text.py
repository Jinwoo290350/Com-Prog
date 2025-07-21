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
'''

def getMultilinesInput():
    text = ""
    while True:
        try:
            line = input()
            if not line:
                break
            text += line + ' '
        except EOFError:
            break
    return text

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
ss = getMultilinesInput()
k = int(input("Top K rank: "))

cleaned_text = ''
for ch in ss:
    if ch.isalpha() or ch.isspace():
        cleaned_text += ch.lower()
    else:
        cleaned_text += ' '

words = cleaned_text.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

bucket = {}
for word in freq:
    count = freq[word]
    if count not in bucket:
        bucket[count] = [word]
    else:
        bucket[count].append(word)

sorted_counts = []
for count in bucket:
    sorted_counts.append(count)

# Manual sort descending
for i in range(len(sorted_counts)):
    for j in range(i + 1, len(sorted_counts)):
        if sorted_counts[j] > sorted_counts[i]:
            sorted_counts[i], sorted_counts[j] = sorted_counts[j], sorted_counts[i]

output = []
rank = 0
last_count = None
for count in sorted_counts:
    group = bucket[count]

    # Manual sort words in group
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if group[j] < group[i]:
                group[i], group[j] = group[j], group[i]

    for word in group:
        output.append((word, count))

    if rank < k:
        rank += 1
        last_count = count
    elif count == last_count:
        continue
    else:
        break

# Re-bucket for printing
final_output = {}
for word, count in output:
    if count not in final_output:
        final_output[count] = [word]
    else:
        final_output[count].append(word)

final_counts = []
for c in final_output:
    final_counts.append(c)

# Manual sort again
for i in range(len(final_counts)):
    for j in range(i + 1, len(final_counts)):
        if final_counts[j] > final_counts[i]:
            final_counts[i], final_counts[j] = final_counts[j], final_counts[i]

for count in final_counts:
    group = final_output[count]

    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if group[j] < group[i]:
                group[i], group[j] = group[j], group[i]

    line = ''
    for i in range(len(group)):
        line += group[i] + ": " + str(count)
        if i != len(group) - 1:
            line += ", "
    print(line)