import math

def formula():
    
    h = 30
    c = 50
    d = input("Please, introduce a sequence of comma separeted numbers:")
    d = d.split(",")
        
    list = []
    for num in d:
        list.append(round(math.sqrt(2 * c * int(num.strip()) / h)))

    return list
        
print(formula())