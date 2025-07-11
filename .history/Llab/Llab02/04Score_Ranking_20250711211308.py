# Score Ranking

y = []
while True:
    x = input("Enter score (or just ENTER to finish): ")
    if x == "":
        break
    else:
        y.append(int(x))

for i in range(y)):
    for j in range(i + 1, len(y)):
        if y[i] < y[j]:
            y[i], y[j] = y[j], y[i]        