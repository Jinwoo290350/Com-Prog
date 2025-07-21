'''
Missing and Additional Values
Given two lists, find the missing and additional values in both the lists.

Examples:
Input:  list1 = [1, 2, 3, 4, 5, 6] 
        list2 = [4, 5, 6, 7, 8] 
Output:  Missing values in list1 = [8, 7] 
         Additional values in list1 = [1, 2, 3] 
         Missing values in list2 = [1, 2, 3] 
         Additional values in list2 = [7, 8] 

ตัวอย่างการทำงาน 1
Input list1: [1, 2, 3, 4, 5, 6]
Input list2: [4, 5, 6, 7, 8]
Missing values in list1 = [7, 8]
Additional values in list1 = [1, 2, 3]
Missing values in list2 = [1, 2, 3]
Additional values in list2 = [7, 8]

ตัวอย่างการทำงาน 2
Input list1: ['1', 2, 3, '4', 5, 6]
Input list2: [4, '5', 6, 7, 8]
Missing values in list1 = [4, '5', 7, 8]
Additional values in list1 = ['1', 2, 3, '4', 5]
Missing values in list2 = ['1', 2, 3, '4', 5]
Additional values in list2 = [4, '5', 7, 8]

ตัวอย่างการทำงาน 3
Input list1: [True, False, None, (), '']
Input list2: []
Missing values in list1 = []
Additional values in list1 = [True, False, None, (), '']
Missing values in list2 = [True, False, None, (), '']
Additional values in list2 = []
'''

x = input("Input list1: ")
list1 = eval(x)
y = input("Input list2: ")
list2 = eval(y)
missing_in_list1 = [item for item in list2 if item not in list1]
additional_in_list1 = [item for item in list1 if item not in list2]
missing_in_list2 = [item for item in list1 if item not in list2]
additional_in_list2 = [item for item in list2 if item not in list1]
print(f"Missing values in list1 = {missing_in_list1}")
print(f"Additional values in list1 = {additional_in_list1}")
print(f"Missing values in list2 = {missing_in_list2}")
print(f"Additional values in list2 = {additional_in_list2}")