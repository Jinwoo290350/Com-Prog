def  plus(total,value):
    total += value
    return total
def  minus(total,value):
    total -= value
    return total

x = int(input("How many food you have : "))

for i in range(x):
    food = input()
    total,value = food.split()
    total = int(total)
    value = int(value)
    if value > 0:
        total = plus(total, value)
    else:
        total = minus(total, value)
    print(f"{total}")
