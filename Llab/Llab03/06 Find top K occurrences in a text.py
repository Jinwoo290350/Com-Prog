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
        line = input()
        if not line:
            break
        text += line + ' '
    return text

def count_words(text):

    words = text.lower().split()

    word_count = {}
    for word in words:
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:  # ถ้าคำไม่ว่าง
            word_count[clean_word] = word_count.get(clean_word, 0) + 1
    
    return word_count

def get_top_k_words(word_count, k):

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    result = []
    current_rank = 0
    
    i = 0
    while i < len(sorted_words) and current_rank < k:
        current_count = sorted_words[i][1]
        same_count_words = []

        while i < len(sorted_words) and sorted_words[i][1] == current_count:
            same_count_words.append(sorted_words[i][0])
            i += 1
        
        result.append((current_count, same_count_words))
        current_rank += 1
    
    return result

def print_results(top_k_results):
    for count, words in top_k_results:
        if len(words) == 1:
            print(f"{words[0]}: {count}")
        else:
            sorted_words = sorted(words)
            words_str = ", ".join([f"{word}: {count}" for word in sorted_words])
            print(words_str)

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
text = getMultilinesInput()
k = int(input("Top K rank: "))
word_count = count_words(text)
top_k_results = get_top_k_words(word_count, k)
print_results(top_k_results)
