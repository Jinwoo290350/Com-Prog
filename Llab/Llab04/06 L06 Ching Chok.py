'''
Ching Chok
พี่ๆCPEได้จัดกิจกรรมชิงโชคเพื่อแจกรางวัลให้กับน้องๆ ในการชิงโชคครั้งนี้ทำมีการหลักในการสุ่มคือ พี่ๆจะเลือกเลขนำโชคมา1ตัว(0-9) แล้วดูว่าเลขบัตรประชาชนของใครมีเลขตรงกับเลขนำโชคมากที่สุด คนนั้นจะได้รับของรางวัลไป

แต่ถ้ามีคนที่มีเลขตรงกับเลขนำโชคเท่ากัน จะดูว่าเลขบัตรประชาชนของใครมีค่ามากกว่ากัน

Example 1
Enter lucky number : 1
Enter amount of candidates : 3
Enter ID card number 1: 123456789
Enter ID card number 2: 112345678 
Enter ID card number 3: 111234567 
Winner: 111234567
Example 2
Enter lucky number : 3
Enter amount of candidates : 4
Enter ID card number 1: 4521163145362
Enter ID card number 2: 1245613124659
Enter ID card number 3: 2124313621364
Enter ID card number 4: 2156489723233
Winner: 2156489723233
Example 3
Enter lucky number : 9
Enter amount of candidates : 5
Enter ID card number 1: 5641239949
Enter ID card number 2: 9459621549
Enter ID card number 3: 3125487623
Enter ID card number 4: 9216945962
Enter ID card number 5: 2154869523
Winner: 9459621549

[hide line #]

'''

x = int(input("Enter lucky number : "))
y = int(input("Enter amount of candidates : "))
z = []

for i in range(y):
    o = input(f"Enter ID card number {i+1}: ")
    z.append(o)

vul = []
for k in z:
    count = k.count(str(x))
    vul.append(count)

max_index = 0
for i in range(1, len(vul)):
    if vul[i] > vul[max_index]:
        max_index = i
    elif vul[i] == vul[max_index]:
        if sum(map(int, z[i])) > sum(map(int, z[max_index])):
            max_index = i

print(f"Winner: {z[max_index]}")
