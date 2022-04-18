input_data = input("Please, introduce a sentence ")

Upper_case = 0
Lower_case = 0

for i in input_data:
    if i.islower():
        Lower_case += 1 
    elif i.isupper():
        Upper_case += 1

print(Lower_case, Upper_case)