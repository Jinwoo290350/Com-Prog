def  plus(total,value):
    total += value
    return total
def  minus(total,value):
    total -= value
    return total

x = int(input("How many food you have : "))

for i in range(x):
    food = input("What food you have : ")
    if food == "apple":
        x = plus(x, 1)
    elif food == "banana":
        x = minus(x, 1)
    elif food == "orange":
        x = minus(x, 2)
    else:
        print("I don't know this food")