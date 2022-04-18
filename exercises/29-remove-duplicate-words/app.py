input_data = input("Please, introduce a sequence of lines:")
input_data = input_data.split(" ")

mylist = []
for i in input_data:

    if i not in mylist:
        mylist.append(i.strip())
        mylist.sort()

    
print(mylist)