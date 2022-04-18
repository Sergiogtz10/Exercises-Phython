data = input("Please, introduce a sequence of comma separeted numbers:" )
data = data.split(",")
list = []
for i in data :
    list.append(i.strip())
print(list)

#El strip()método elimina cualquier carácter inicial (espacios al principio) y final (espacios al final)

