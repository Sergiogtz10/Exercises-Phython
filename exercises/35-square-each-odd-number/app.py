input_data = input("Please, introduce a sequence of numbers separate for commas:")
input_data = input_data.split(",")

mylist = []

for i in input_data:
    i = int(i)
    if i % 2  != 0:
        mylist.append(i)

    
print(mylist)