data = input("Enter a comma separated details: ")
list = [detail.split(",") for detail in data.split(" ")] 
print(sorted(list))