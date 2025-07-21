'''
[best quiz upgrade] อาจารย์ใจดีจังเลยแต่ใจดีน้อยลง
วิชา Computer Programming ของอาจารย์โตโต้มีนิสิตลงเรียนหลายคน และมีการสอบย่อยทั้งหมดหลายครั้ง อาจารย์โตโต้ต้องการพิมพ์ชื่อนิสิตที่คะแนนดีที่สุด โดยการวัดคะแนนนั้น ในที่นี้จะไม่นับการสอบครั้งที่มีคะแนนการสอบย่อยครั้งที่ได้คะแนนน้อยที่สุด 1 ครั้ง (กรณีที่คะแนนน้อยที่สุดมีมากกว่า 1 ครั้ง จะตัดออกเพียงครั้งเดียวเท่านั้น) และจะไม่นับการสอบครั้งที่มีคะแนนการสอบย่อยครั้งที่ได้คะแนนมากที่สุด 1 ครั้ง (กรณีที่คะแนนมากที่สุดมีมากกว่า 1 ครั้ง จะตัดออกเพียงครั้งเดียวเท่านั้น) เช่น ถ้าได้คะแนนสอบ 10 9 7 7 8 คะแนนที่ดีที่สุดจะเป็น 9+7+8

จงเขียนโปรแกรมรับข้อมูล โดยรับค่าไฟล์ที่มีข้อมูลด้านในประกอบด้วย ชื่อนิสิต และคะแนนการสอบแต่ละครั้งใน 1 แถว เช่น

Non 9 8 7 8 8
Prince 3 5 4 2 10
Khanun 7 7 9 9 6
Plapud 0 9 7 8 10
Queen 10 7 7 8 7
โดยให้แสดงคะแนนที่สูงที่สุด และ รายชื่อผู้ที่ได้คะแนนสูงสุด อาจมีมากกว่า 1 คนโดยรายชื่อจะเรียงตามข้อมูลนำเข้า

Example
File name: Example.txt
24
Non
Plapud
'''

filename = input("File name: ")
students = []
scores = []
adjusted_scores = []

with open(filename, 'r') as file:
    for line in file:
        data = line.strip().split()
        name = data[0]
        student_scores = list(map(int, data[1:]))
        
        students.append(name)
        scores.append(student_scores)
        
        student_scores_copy = student_scores.copy()
        student_scores_copy.remove(max(student_scores_copy))
        student_scores_copy.remove(min(student_scores_copy))
        
        adjusted_scores.append(sum(student_scores_copy))

max_score = max(adjusted_scores)
print(max_score)

for i in range(len(students)):
    if adjusted_scores[i] == max_score:
        print(students[i])