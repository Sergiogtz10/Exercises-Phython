def Number(number):
    x = 0
    while x < number:
        y = x
        x = x + 1
        if y % 7 == 0:
            yield y

for x in Number(50):
    print(x)