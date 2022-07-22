class Car:
	def __init__(self, name , model , year, fuel):
		
		self.name = name
		self.model = model
		self.year = year
		self.fuel = fuel
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

	def no_fuel(self):
		print(f"Car Have {self.fuel}")
			
audi = Car('audi','a4',2019,'No Gas')
#print(audi.fulldes_car())

#audi.no_fuel()

#audi.update_meter(23_100)
#audi.odo_meter()

#audi.increment_miles(100)
#audi.odo_meter()
class Battery:
	def __init__(self, battery_size=75):
		self.battery_size = battery_size
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")
	def upgrade_battery(self):
		self.battery_size = 100
	def get_range(self):
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"If Car Once Fully Charged, This Car Can Go {range} Miles")

class ElectriCar(Car):
	def __init__(self,make,model,year,fuel):
		super().__init__(make,model,year,fuel)
		self.battery = Battery()

	#def des_battery(self):
		#print(f"This Car Have {self.battery}-KWH Battery")

	def no_fuel(self):
		if self.fuel: 
			print("This Is An Electric Car")

electricar = ElectriCar('tesla','model s',2018,'fuel')
#print(electricar.fulldes_car())

#electricar.no_fuel()
#electricar.battery.describe_battery() 	`	=PIUJIOP[]';LMN BNK,#electricar.battery.get_range()
#electricar.battery.upgrade_battery()
#electricar.battery.get_range()


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

#pooja_hotel = Restaurant('Salt Bees','American Fusion',"Open")
#pooja_hotel.des_res()
#pooja_hotel.status_res()#pooja_hotel.cuisine()#pooja_hotel.num_of_cus = 19
#pooja_hotel.update_numofcus(8)#pooja_hotel.increment_numofcus(2)
#pooja_hotel.numof_cus()
#print(f"Our Restaurant is {pooja_hotel.status} at Monday To Sunday  24/7")

class IceCreamStand(Restaurant):
	def __init__(self,res_type,cuisine_type,status,flavors):
		super().__init__(res_type,cuisine_type,status)
		self.flavors = flavors
	def available_flavors(self):
		print(f"The Available {self.flavors} Are Strawberry, Chocolate, Vennila ")
muniyandi = IceCreamStand("Hotel Muniyandi",'Classical indian','Open','flavors')
#muniyandi.des_res()
#muniyandi.available_flavors()

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

#Vignes = User('Vignesh','joining',"Porayar","19")
#Vignes.increment_login(2)
#Vignes.usrlogin()
#Vigne.reset_login()


#Vignes.name()
#Vignes.greeting()
#print(f'Im {Vignes.info} , My Age is {Vignes.age} and I\'m From {Vignes.town}')
#print(f"Thanks for {Vignes.greet} {Vignes.info}")
class Privillege:
	
	def __init__(self,privillege='Admin Privilleges'):
		self.privillege = privillege
	
	def admin_privilleges(self):
		privll = ['can add a post','can delete a post','can ban user']
		print(f"{self.privillege} are {privll}") 

class Admin(User):
	def __init__(self,info,greet,town,age,privilleges):
		super().__init__(info,greet,town,age)
		self.privilleges = privilleges
		self.privillege = Privillege()
	
	def show_privilleges(self):
		print(f"The {self.privilleges} Privilleges are 1.Can Bann User, 2.Can Add User")

akas = Admin('Akash',"HI","PYR","18",'Admin')
#akas.show_privilleges()
#akas.privillege.admin_privilleges()