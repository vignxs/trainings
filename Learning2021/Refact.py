import json

# def greet_user():
#     file = "user.json"
#     try:
#         with open(file) as f:
#     	    name = json.load(f)
#     except FileNotFoundError:
#         user = input("Enter Your Name : ")
#         with open(file,"w") as f:
#             json.dump(user,f)
#         print(f"We'll Remember You When You Come Back {user}")
#     else:	   
#         print(f"I Remember You {name}")
# greet_user()

# import json

# def usr_name():
#     filename = "user.json"
#     try:
#         with open(filename) as f:
#             name = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return name

# def greet():
#     user = usr_name()
#     if user:
#         print(f" I Remember You {user} ")
#     else:
#         filename = "user.json"
#         user = input("What Is Your Name : ")
#         with open(filename,"w") as f:
#             json.dump(user,f)
#         print(f" We'll Remember You Next Time When You ComeBack {user}")
    
# greet()

###Full Remember_me

def get_name():
    filename = "user.json"
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name

def new_name():
    user = input("What Is Your Name : ")
    filename = "user.json"
    with open(filename,"w") as f:
        json.dump(user,f)
        
def greet():
    name = get_name()
    tell = input(f"Is This Your Name - {name} IF It Is Enter Yes OR No :) ")
    if tell  == "yes" :
        print(f" I Remember You {name}")
    else:
        name = new_name()
        print(f"We'll Remember You When YouComeback {name}")

greet()


###Fav NUmber
# filename = "fav_num.json"
# try:
#     with open(filename) as f:
#         name = json.load(f)
# except FileNotFoundError:
#     fav = input("Enter Your Favorite Number : ")
#     with open(filename,"w") as f:
#         json.dump(fav,f)
#     print(f"I Got Your NUmber {fav}")
# else:
#     print(f"I Know Your Favorite Number {name}")

   