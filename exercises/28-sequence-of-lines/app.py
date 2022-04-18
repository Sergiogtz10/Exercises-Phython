input_data = input("Please, introduce a sequence of comma separeted lines:")
input_data = input_data.split(",")

list = []
for i in input_data:
    list.append(i.strip().upper())
    
    
print(list)