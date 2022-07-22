# response = {}

# def test():
#     name = input("Enter your name : ")
#     age = input("Enter your age : ")
#     mail = input("Enter your mailid : ")
#     place = input("Enter where you belong : ")
#     by = input("Enter your birth year : ")
#     if len(name) == 0 or len(age) == 0 or by == 0:
#         print("Seems Like You Forget to Enter Some of the Values , Please Re-Enter Again")
#         test()
#     else:
#         response['name'] = name
#         response['age'] = age
#         response['mail'] = mail
#         response['place'] = place
#         response['birth year'] = by


# print("I need your personal details")
# fvr= input("To get started Enter \"yes\"")
# if fvr.lower() == 'yes':
#     test()
 

# print("---- Results ----")
# for k,v in response.items():
#     print(f"{k.upper()} - {v.upper()}")


# 
responses = {}

#flag
poll = True

while poll:
        name=(input('tell me your name : '))
        resp=(input('which is your favorite country : '))
        
        #storing
        responses[name]=resp
        
        hi =(input('would you let another one try enter Yes/no'))
        
        if hi == "no":
            poll = False
print("\n Pool Results ")
for i,v in responses.items():
    print(f"Hi Im {i}, i want to go {v}")