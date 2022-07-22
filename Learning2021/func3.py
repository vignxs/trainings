def food(*toop):
	print('the foods are')
	for f in toop:
		print(f"hi in {f}")
food('hi','bye')

def make_pizza(size,*topping):
	print(f"{size} inch pizza and what topping  you want")
	for  topp in topping:
		toop = topp
		print(toop)
make_pizza(16,"chilly",'pepper')

def profile(first ,last , **userinfo):
	userinfo['firstname']=first
	userinfo['lastname']=last
	print(userinfo)
hi = profile('vig','nesh',
			hi='bye',)
print(hi)


def pizz(list2):
	print('pizza are  ready wanna try')

	for i in list2:
		print(f"-   {i}")
hi =['hot','chilly','chezzy']
pizz(hi)


def info(first, last , **user):

	user[first_name]= first
	user[last_name] = last

	return user

cu = profile("vignesh", 'sivakumar',
				location='porayar',
				status= 'poor')
print(cu)


def models(first, last , **info):

	info['name']= first
	info['model_number'] = last

	return info

car = models("audi", 'G38',
				location='porayar',
				color= 'blue',
				speed=True)
print(car)

import bot

u = build_profile("audi", 'G38',
				location='porayar',
				color= 'blue',
				speed=True)
print(u)