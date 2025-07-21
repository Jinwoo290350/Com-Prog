'''
Binary Search
คุณเป็นผู้ช่วยนักวิจัยที่ต้องค้นหาข้อมูลจากฐานข้อมูลขนาดใหญ่ที่จัดเรียงไว้แล้ว วิธีที่เร็วที่สุดคือการใช้เทคนิค Binary Search ซึ่งทำงานโดย:

หาตัวตรงกลาง (mid) ของช่วงข้อมูลที่กำลังดูอยู่ ถ้าตำแหน่งมีเศษให้ปัดลง
เปรียบเทียบค่าตรงกลางกับค่าที่ต้องการหา (target)
ถ้าเท่ากัน: พบข้อมูลแล้ว!
ถ้าน้อยกว่า: ค้นหาต่อทางขวาของ mid
ถ้ามากกว่า: ค้นหาต่อทางซ้ายของ mid
diagram

จงเขียนโปรแกรมเพื่อนับจำนวนครั้งที่ต้องทำ Binary Search เพื่อค้นหาค่า target ในลิสต์ข้อมูลที่เรียงลำดับแล้ว

ตัวอย่างการทำงาน

ตัวอย่างที่ 1:

ข้อมูล: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
ค่าที่ต้องการหา: 7
จำนวนครั้งที่ค้นหา: 4
ตัวอย่างที่ 2:

ข้อมูล: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
ค่าที่ต้องการหา: 16
จำนวนครั้งที่ค้นหา: 2
'''

def binary_search_count(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0 
    
    while low <= high:
        count += 1 
        mid = (low + high) // 2 
        
        if arr[mid] == target:
            return count 
        elif arr[mid] > target:
            high = mid - 1 
        else:
            low = mid + 1  
    
    return count 

sorted_list = list(map(int, input("ข้อมูล: ").split(',')))
target_value = int(input("ค่าที่ต้องการหา: "))
search_count = binary_search_count(sorted_list, target_value)
print(f"จำนวนครั้งที่ค้นหา: {search_count}")