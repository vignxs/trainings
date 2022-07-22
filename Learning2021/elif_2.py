av_t =['muss','pepe','oliv']
r_t=["fries",'pepe','grp']
for r in r_t:
	if r in av_t:
		print(f"you can have {r} ")
	else:
		print('you can\'t sry')
nms = ['ada','conor','khabib','joe','admin']
for n in nms:
	if  n == "admin":
		print("hey, admin wanna see the status")
	else:
		print(f"hello,{n} welcome")
i=[]
if  i:
	for x in i:
		print('hi')
else:
	print('need  usrs')

c_u =['john','ada','wadur','boah','noah','niyoo']
n_u=['john','vi','hey','wadur','noah']
for n in n_u:
	if n in c_u:
		print("name is taken")
	else:
		print("you\'re good to go")

for x in range(11):
	if x == 1:
		print(f'{str(x)}st')
	elif x == 2:
		print(f'{str(x)}nd')
	elif x == 3:
		print(f'{str(x)}rd')
	elif x >=4:
		print(f'{str(x)}th')