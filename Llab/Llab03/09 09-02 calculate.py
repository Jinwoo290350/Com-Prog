'''
[calculate] เครื่องคิดเลขใช้ถ่ายรูปไม่ได้นะรู้เปล่า?
   ให้นิสิตเขียนโปรแกรมรับเลขหนึ่งจำนวน (num) และ ตัวเลขที่ต้องการนำมาหาว่ามาสามารถหารเลขตัวแรกลงตัวไหม(k) แล้วหาว่าเป็นดังข้อต่อไปนี้หรือไม่
       > เป็นเลขคู่หรือไม่ ?
       > factorial ของค่านั้น ? (หากเลขดังกล่าวมีค่ามากกว่า 20 ให้แสดง TOO LONG)
       > เป็น prime number หรือไม่ ?
       > หารด้วย k ลงตัวหรือไม่ ?
       > เป็นเลขอะไรในระบบเลขฐาน 2 ?
       > เป็นเลขอะไรในระบบเลขฐาน 8 ?
       > เป็นเลขอะไรในระบบเลขฐาน 16 ?
       > เป็นเลขอะไรในระบบเลขโรมัน ?
       > แสดงค่า pi จากการคำนวณสมการ Nilakantha pi 
3
+
4
2
∗
3
∗
4
−
4
4
∗
5
∗
6
+
4
6
∗
7
∗
8
−
.
.
.
 โดยคำนวณเฉพาะ 50 พจน์แรก ไม่นับค่าคงที่ 3 ตัวแรก

Sample Output 1
Please Enter Number : 10
Divide by? : 2
This number is even number.
factorial is 3,628,800.
This number is not a prime number.
10 is divisible by 2.
10 is 1010 in base 2.
10 is 12 in base 8.
10 is A in base 16.
10 is X in roman numeral system.
PI is 3.14159076984979535041
Sample Output 2
Please Enter Number : 59
Divide by? : 3
This number is not even number.
factorial TOO LONG.
This number is a prime number.
59 is not divisible by 3.
59 is 111011 in base 2.
59 is 73 in base 8.
59 is 3B in base 16.
59 is LIX in roman numeral system.
PI is 3.14159076984979535041
Sample Output 3
Please Enter Number : 77
Divide by? : 7
This number is not even number.
factorial TOO LONG.
This number is not a prime number.
77 is divisible by 7.
77 is 1001101 in base 2.
77 is 115 in base 8.
77 is 4D in base 16.
77 is LXXVII in roman numeral system.
PI is 3.14159076984979535041
Sample Output 4
Please Enter Number : 82
Divide by? : 41
This number is even number.
factorial TOO LONG.
This number is not a prime number.
82 is divisible by 41.
82 is 1010010 in base 2.
82 is 122 in base 8.
82 is 52 in base 16.
82 is LXXXII in roman numeral system.
PI is 3.14159076984979535041

[hide line #]

'''

import math

class MyMath:
    def __init__(self):
        self.pi = self.calculate_pi_nilakantha()
    
    def is_even(self, num):
        return num % 2 == 0
    
    def fac(self, num):
        return math.factorial(num)
    
    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    def divide_by(self, num, k):
        return num % k == 0
    
    def ten_to_bi(self, num):
        return bin(num)[2:]
    
    def ten_to_oct(self, num):
        return oct(num)[2:]
    
    def ten_to_sixteen(self, num):
        return hex(num)[2:].upper()
    
    def int_to_roman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num
    
    def calculate_pi_nilakantha(self):
        pi = 3.0
        sign = 1
        for i in range(1, 51):
            n = 2 * i
            term = 4 / (n * (n + 1) * (n + 2))
            pi += sign * term
            sign *= -1
        return pi
    
'''
# do not submit this code!!!
my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')
'''