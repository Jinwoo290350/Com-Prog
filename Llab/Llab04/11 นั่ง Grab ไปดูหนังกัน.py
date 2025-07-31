groups = list(map(int, input().split()))
groups.sort(reverse=True)
cars = 0

while groups:
    capacity = 4
    i = 0
    while i < len(groups):
        if groups[i] <= capacity:
            capacity -= groups[i]
            groups.pop(i)
        else:
            i += 1
    cars += 1

print(cars)
