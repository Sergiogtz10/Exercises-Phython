def generate_dict(number):

    mydict = {}
    for i in range(0, number):
        mydict[i] = i * i
    return mydict
print(generate_dict(8))


