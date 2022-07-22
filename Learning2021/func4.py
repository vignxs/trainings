import bot

u=  bot.build_profile("audi", 'G38',
				location='porayar',
				color= 'blue',
				speed=True)
print(u)

nums = [1,2,3,4,5,6]
even = []
odd = []

for x in nums:
	if x % 2 == 0:
		even.append(x)
	else:
		odd.append(x)

print(sum(even))
print(sum(odd))

print(nums[::-1])