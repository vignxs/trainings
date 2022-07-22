def count(filename):
    try :
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError :
        #pass
        print("file is missing or misspelled")
    else:
        #word = content
        print(content)

file =["cat.txt","py.txt","dog.txt"]
for filename in file:
    print(count(filename))

import json

numbers = [2,4,5,6,9,5]

filename = 'numbers.json'
with open(filename,"w") as  f:
    json.dump(numbers,f)

#import json

filename = "numbers.json" 
with open(filename) as f:
    numbers = json.load(f)
    print(numbers)

file = "im vignes"
filename = "foods.json"
with open(filename,"w") as f:
    json.dump(file,f)

#idk
user = input("Enter Your Name : ")
filename = "user.json"

with open(filename,"w") as f:
    json.dump(user,f)
    #print(f"We'll Remember You When You Come Back {user}")


import json

file = "user.json"
try:
    with open(file) as f:
        name = json.load(f)
except FileNotFoundError:
    user = input("Enter Your Name : ")
    with open(file,"w") as f:
        json.dump(user,f)
    print(f"We'll Remember You When You Come Back {user}")
else:	   
     print(f"I Remember You {name}")