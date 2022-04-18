string = input("Write New to Python or choosing between Python 2 and Python 3")
string = string.split()

data = set(string) 
data = sorted(data) 

for x in data:
    print(f"{x}: {string.count(x)}")