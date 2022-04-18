
numbers = input("Write a comma separated 4 numbers in binary: ")
numbers = numbers.split(",")

data = list(filter(lambda i: int(i, 2) % 5 == 0, numbers))  
print(",".join(data))