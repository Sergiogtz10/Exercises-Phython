list_even = []
for x in range(1000, 3001):
    data = str(x)
    even = True

    for y in data:
        y = int(y)
        if y % 2 != 0:
            even = False

    if even:
        list_even.append(x)

print(list_even)