def getMultilinesInput():
    x = ""
    while True:
        y = input()
        if not y:
            break
        x += y + ' '
    return x

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
x = getMultilinesInput()

x = x.lower().split()

k = int(input("Top K rank: "))

y = {}
for i in x:
    y[i] = y.get(i, 0) + 1

x = sorted(y.items(), key=lambda _: (-_[1], _[0]))

i = 0
j = 0

while j < k and i < len(x):
    _ = x[i][1]
    __ = []
    
    while i < len(x) and x[i][1] == _:
        __.append(x[i][0])
        i += 1
    
    print(", ".join(f"{y}: {_}" for y in __))
    j += 1