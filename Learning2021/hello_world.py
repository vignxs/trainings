# 
responses = {}

#flag
poll = True

while poll:
        name=(input('tell me your name : '))
        resp=(input('which is your favorite country : '))
        
        #storing
        responses[name]=resp
        print(responses)
        hi =(input('would you let another one try enter Yes/no'))
        
        if hi == "no":
            poll = False
print("\n Pool Results ")
for i,v in responses.items():
    print(f"Hi Im {i}, i want to go {v}")