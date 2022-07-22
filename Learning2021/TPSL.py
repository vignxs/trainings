from random import randint
#print(randint(1,100))
from random import choice

class Die:
	def __init__(self):
		self.die=6
	def roll_die(self):
		hi = randint(1,6)
		print(hi)
gdie = Die()

gdie.roll_die()

c = 1
while c == 4:
	num = randint(1,10)
	print(num)
	c += 1


