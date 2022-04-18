

# Input instruccions  
'''
 At least 1 letter between [a-z].
At least 1 number between [0-9].
At least 1 letter between [A-Z].
At least 1 character from [$#@].
Minimum length of transaction password: 6.
Maximum length of transaction password: 12.
'''
import re
password=input("Enter a comma separated string: ")

values = list(password.split(","))

list = []
sequence= "^.*(?=.{6,12})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$]).*$"

for value in values:
    result = re.findall(sequence, value)
    if result:
        list.append(result)
if not list:
    print("Error")
else:
    print(list)