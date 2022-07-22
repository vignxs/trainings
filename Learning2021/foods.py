foods=['dosa',"dosa",'idly','chutney',"dosa",'sambar']
food=[]
while foods:
    c=foods.pop()
    
    print(f"i made your {c}")
    
    food.append(c)

for f in food:

    print(f" {f}")

print(f' we are running out of {food[-1]}')\

while "dosa" in food:
    food.remove('dosa')

print(food)



poll = True
responses={}
while poll:
    name=(input('tell me your name'))
    respo=(input('love r arranged'))
    
    responses[name]=respo
    
    hi=(input('would you let another one try yes/no '))
    if hi == 'no':
        poll=False
        
print('-----Poll Results-----')
for i,v in responses.items():
    print(f"Hi im {i}, i like {v} marriages")
    