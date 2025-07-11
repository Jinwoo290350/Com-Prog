def  plus(total,value):
    total += value
    return total
def  minus(total,value):
    total -= value
    return total

x = int(input("How many food you have : "))

for i in range(x):
    food = input()
    amount, status = food.split()
    amount = int(amount)
    status = int(status)
    if status == 1:
        total = plus(total, amount)
    elif status == -1:
        total = minus(total, amount)
    else:
        print("สภาพอาหารต้องเป็น 1 หรือ -1 เท่านั้น")

print(f"{total}")
