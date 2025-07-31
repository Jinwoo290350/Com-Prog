'''
CommaCode
เพื่อให้โปรแกรมสามารถทำงานได้ตามตัวอย่าง
ให้นิสิตสร้าง function ชื่อ commaCode(myList) ซึ่งรับ parameter 1 ตัวชื่อ myList
โดยที่ function นี้จะ return เป็น string ของ value ที่อยู่ใน myList ทั้งหมด คั่นด้วย comma และช่องว่าง นอกจากนี้เมื่อถึง value ตัวสุดท้ายของ myList ให้เชื่อมด้วย and แล้วตามด้วย value ตัวสุดท้าย

note: พบการใช้คำสั่ง join หรือ import ไลเบรรี่พิเศษใด หักแต้มที่ได้ 70%

Example 1
Input: apples bananas tofu cats
apples, bananas, tofu, and cats
>>> 
Example 2
Input: cpe35
cpe35
>>> 
Example 3
Input: 
>>>

Examples 1 (shell mode)
>>> myList = ['apples','bananas','tofu','cats']
>>> commaCode(myList)
apples, bananas, tofu, and cats
>>> 
Examples 2 (shell mode)
>>> myList = ['cpe35']
>>> commaCode(myList)
cpe35
>>> 
Examples 3 (shell mode)
>>> myList = []
>>> commaCode(myList)
''
>>> 
Send only your commaCode() function below.
'''

def commaCode(myList):
    ans = ""
    for i in range(len(myList)):
        if i == 0:
            ans += myList[i]
        elif i == len(myList) - 1:
            ans += " and "+myList[i]
        else:
            ans += ", "+myList[i]
    return ans
            
s = input("Input: ").split()
r = commaCode(s)
print(r)