input_data = input("Please introduce here your sentence and digits ")

Letters = 0
Digits = 0

for i in input_data:
    if i.isalpha():
        Letters += 1 
    elif i.isnumeric():
        Digits += 1

print(Letters, Digits)