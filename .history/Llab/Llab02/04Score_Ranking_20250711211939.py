# Score Ranking

y = []
while True:
    x = input("Enter score (or just ENTER to finish): ")
    if x == "":
        break
    else:
        y.append(int(x))

for i in (y):
    if i < 0 or i > 100:
        print("Invalid score, please enter a score between 0 and 100.")
        y.remove(i)
        y.sort(reverse=True)
y.sort(reverse=True)    

for i in y:
    print(f"Rank #{len(y)}: {i}")
   