'''
Dictionary
ให้น้องๆทำdictionaryขนาดย่อมที่มีคำศัพท์คือ arm (n) แขน, hello (v) สวัสดี, beautiful (adj) สวย, toilet (n) ห้องน้ำ, kick (v) เตะ, handsome (adj) หล่อ

โดยที่บรรทัดแรกรับคำในdictนั้น ถ้าไม่เจอในdictให้แสดงว่า Word not in dictionary. และจำรับคำจนกว่าจะเจอ บรรทัดต่อมารับค่า โดยที่ถ้าเป็น1 จะแสดงชนิดของคำศัพท์นั้น ถ้าเป็น2 จะแสดงคำแปลของคำนั้น แต่ถ้าไม่ใช่1หรือ2ให้แสดงว่า Invalid option. และรับค่าจนกว่าจะถูก

โปรแกรมจะหยุดทำงานเมื่อwordเป็น 0

Example 1
arm
1
n
arm
2
แขน
handsome
1
adj
handsome
2
หล่อ
0
Example 2
toilet 
1
n
toilett
Word not in dictionary.
toilet
3
Invalid option.
1
n
0 
Example 3
beautiful
1
adj
beautiful
2
สวย
kick
3
Invalid option.
p 
Invalid option.
2
เตะ
0
'''

x = {"arm":{1:"n",2:"แขน"}, "hello":{1:"v",2:"สวัสดี"}, "beautiful":{1:"adj",2:"สวย"}, "toilet":{1:"n",2:"ห้องน้ำ"}, 
     "kick":{1:"v",2:"เตะ"}, "handsome":{1:"adj",2:"หล่อ"}
     }

while True:
    word = input().strip()
    if word == "0":
        break
    elif word in x:
        while True:
            num_input = input().strip()
            if num_input.isdigit():
                number = int(num_input)
                if number in x[word]:
                    print(f"{x[word][number]}")
                    break
                else:
                    print("Invalid option.")
            else:
                print("Invalid option.")
    else:
        print("Word not in dictionary.")

#การใช้ dictionary และการรับinput แบบ loop กับ dictionary