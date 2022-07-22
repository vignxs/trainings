class Dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def sit(self):
		print(f"Hey! my Dog {self.name} is Siting")

	def rollback(self):
		print(f"{self.name} Just Rolled Over, You Missed it")

my_dog = Dog('Willie',9)
your_dog = Dog('Jackie',5)

print(f"My Dog Name is  {my_dog.name} and His Age is {my_dog.age}")
my_dog.sit()
my_dog.rollback()

print(f"\nMy Dog Name is  {your_dog.name} and ")
print(f"His Age is {your_dog.age}")

your_dog.sit()
your_dog.rollback()
print('\n')


print('\n')



print('\n')

class Car:
	def __init__(self,name , model , year):
		
		self.name = name
		self.model = model
		self.year = year
		self.meter = 0

	def fulldes_car(self):
		carz = f'{self.name} {self.model} {self.year}'
		return carz.title()

	def odo_meter(self):
		print(f'This Car Has {self.meter} Miles on  It')

	def update_meter(self,mileage):
		if mileage > self.meter:
			self.meter = mileage
		else:
			print("You Can't Rollback The Meter Value")
	def increment_miles(self,miles):
		self.meter += miles	

audi = Car('audi','a4',2019)
print(audi.fulldes_car())


audi.update_meter(23_100)
audi.odo_meter()

audi.increment_miles(100)
audi.odo_meter()

print('\n')

class Restaurant:
	def __init__(self,res_type,cuisine_type,status,):
		# res = restaurant
		self.res_type = res_type
		self.cuisine_type = cuisine_type
		self.status = status
		self.num_of_cus = 0
	
	def  des_res(self):
		print(f"Hi! , Our Restaurant is {self.res_type} Type ")
	
	def status_res(self):
		print(f"Our Restaurant is {self.status} Now")
	
	def cuisine(self):
		print(f"Our Cuisine is {self.cuisine_type}")

	def numof_cus(self):
		print(f"We Served {self.num_of_cus} Customers Today")

	def update_numofcus(self,num):
		if num > self.num_of_cus:
			self.num_of_cus = num 
		else:
			print('NO Customers Yet !')
	def increment_numofcus(self,extra):
		self.num_of_cus += extra

pooja_hotel = Restaurant('Salt Bees','American Fusion',"Open")

pooja_hotel.des_res()
pooja_hotel.status_res()
pooja_hotel.cuisine()
#pooja_hotel.num_of_cus = 19

pooja_hotel.update_numofcus(8)
pooja_hotel.increment_numofcus(2)
pooja_hotel.numof_cus()


print(f"Our Restaurant is {pooja_hotel.status} at Monday To Sunday  24/7")

print('\n')

class User:		
	def __init__(self,info,greet,town,age):
		self.info = info
		self.greet = greet
		self.town = town
		self.age = age
		self.login_attempt = 0
	
	def name(self):
		print(f"Hi! , My Name is {self.info}")

	def greeting(self):
		print(f"Thanks for {self.greet} Us Today Mr {self.info}") 

	def place(self):
		print(f"I'm From {self.town}")

	def age(self):
		print(f"My Age Is {self.age}")

	def usrlogin(self):
		print(f"Total Login Attempt's {self.login_attempt}")

	def increment_login(self,add):
		self.login_attempt += add
	
	def reset_login(self):
		self.login_attempt = 0
		print(f"login Attempt's Reseted to {self.login_attempt}")

Vignes = User('Vignesh','joining',"Porayar","19")
Vignes.increment_login(2)
Vignes.usrlogin()
Vignes.reset_login()


#Vignes.name()
#Vignes.greeting()
#print(f'Im {Vignes.info} , My Age is {Vignes.age} and I\'m From {Vignes.town}')
#print(f"Thanks for {Vignes.greet} {Vignes.info}")