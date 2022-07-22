class Car:
	def __init__(self, name , model , year  ):
		
		self.name = name
		self.model = model
		self.year = year
		#self.fuel = fuel
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

	#def no_fuel(self):

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
	def __init__(self,make,model,year,):#fuel
		super().__init__(make,model,year,)#fuel
		self.battery = Battery()

	def des_battery(self):
		print(f"This Car Have {self.battery}-KWH Battery")

	#def no_fuel(self):
		#if self.fuel: 
			#print("This Is An Electric Car")
		#print(f"Car Have {self.fuel}")
tesla = ElectriCar('tesla','s',2019,)
