def Two_dimensional(x, y):
    list = []

    for lines in range (0, x):
        line = []
        for cell in range(0, y):
            line.append(lines * cell)

        list.append(line)

    return list

print(Two_dimensional(3, 5))