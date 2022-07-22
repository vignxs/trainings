prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print('message') 

active = True
while active:
    h = input('hi talk or quit')
    if h == 'quit':
        active = False
    else:

msg =('wnter your age  so that i can  tell the cost of ticket or enter 0 to exit')
hi=""
while hi != 0:
    hi = int(input(msg))
    if hi == 0:
        break
    elif hi <= 3:
        print("price is Free")
    elif hi <= 12:
        print('price is 10$')
    else:
        print("price is 20$")


    prompt= ('tell me the city that you want to visit')
>>> prompt+="or enter 'quit' to exit"
>>> while True:
...     h=input(prompt)
...     if h == 'quit':
...             break
...     else:
...             print(f"i would love to visit {h}")

n = 0
>>> while n <= 10:
...     n += 1
...     if n % 2 == 0:
...             continue
...     print(n)
...


 prompt = ("enter the topping  that you want")
>>> prompt +=('or enter quit to exit')
>>> while True:
...     hi=input(prompt)
...     if hi == 'quit':
...             break
...     else:
...             print(hi)
        print(h)

x = 1
while x <= 5 :
	print(x)