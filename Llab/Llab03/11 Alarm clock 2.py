'''
Alarm clock 2
ช่วงนี้กรมอุตุนิยมวิทยาได้พยากรณ์ว่าช่วงนี้มีฝนตกหนัก ทำให้เกิดน้ำท่วมในหลายพื้นที่ ทำให้เกิดการจราจรติดขัด ซึ่งมันส่งผลกระทบต่อการมาเรียนของนิสิตทำให้นิสิตต้องตื่นเช้ามากขึ้นเพื่อให้สามารถเข้าเรียนได้ทันเวลา แต่ตอนเช้านิสิตง่วงไม่อยากตื่นทำให้เมื่อนาฬิกาปลุกนิสิตจึงกดsnoozeหรือdismiss ทำให้เวลาในการตื่นของนิสิตถูกเลื่อนออกไปเรื่อยๆ ดังนั้นอยากให้ทุกคนช่วยกันหาว่านิสิตจะนอนถึงเมื่อไหร่จนกว่านิสิตคนนี้จะตื่น

กำหนดให้

Input current คือ เวลาที่เริ่มนอน โดยระบบเวลาจะใช้รูปแบบ 24 ชั่วโมง (สิ้นสุดวันตอนเวลา 23:59น. และเริ่มวันใหม่ที่เวลา 00:00 น.)
Input nap time คือ จำนวนนาทีในการพักผ่อน โดยการันตีว่าข้อมูลที่รับเข้ามาเป็นจำนวนเต็มบวกเท่านั้น
Input snooze time คือ จำนวนนาทีการเลื่อนปลุกในแต่ละครั้ง โดยการันตีว่าข้อมูลที่รับเข้ามาเป็นจำนวนเต็มบวกเท่านั้น
โดยสามารถinputได้่ว่าว่านิสิตจะกด Snooze หรือ Dismiss โดยที่ Snooze คือการเลื่ือนปลุก และ Dismiss คือการยกเลิกการปลุก
โปรแกรมจะหยุดการทำงานเมื่อ input คือ Dismiss
" ห้ามมีการ import ใดๆทั้งสิ้น "

Sample Output 1
Input current time: 00:00
Input nap time: 3
Input snooze time: 2
Nap time starts.
00:01
00:02
00:03
Alarm rings. Dismiss or Snooze: Snooze
00:04
00:05
Alarm rings. Dismiss or Snooze: Snooze
00:06
00:07
Alarm rings. Dismiss or Snooze: Snooze
00:08
00:09
Alarm rings. Dismiss or Snooze: Snooze
00:10
00:11
Alarm rings. Dismiss or Snooze: Dismiss
Sample Output 2
Input current time: 23:49
Input nap time: 5
Input snooze time: 7
Nap time starts.
23:50
23:51
23:52
23:53
23:54
Alarm rings. Dismiss or Snooze: Snooze
23:55
23:56
23:57
23:58
23:59
00:00
00:01
Alarm rings. Dismiss or Snooze: Snooze
00:02
00:03
00:04
00:05
00:06
00:07
00:08
Alarm rings. Dismiss or Snooze: Dismiss
Sample Output 3
Input current time: 09:50
Input nap time: 5
Input snooze time: 3
Nap time starts.
09:51
09:52
09:53
09:54
09:55
Alarm rings. Dismiss or Snooze: Snooze
09:56
09:57
09:58
Alarm rings. Dismiss or Snooze: Snooze
09:59
10:00
10:01
Alarm rings. Dismiss or Snooze: Snooze
10:02
10:03
10:04
Alarm rings. Dismiss or Snooze: Dismiss

[hide line #]

'''

x = input("Input current time: ")
nap_time = int(input("Input nap time: "))
snooze_time = int(input("Input snooze time: "))
x = x.split(":")
hour = int(x[0])
minute = int(x[1])
print("Nap time starts.")
for i in range(nap_time):
    minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
    print(f"{hour:02}:{minute:02}")
    
while True:
    alam = input("Alarm rings. Dismiss or Snooze: ")
    if alam.lower() == "dismiss":
        break
    elif alam.lower() == "snooze":
        for i in range(snooze_time):
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
            if hour == 24:
                hour = 0
            print(f"{hour:02}:{minute:02}")