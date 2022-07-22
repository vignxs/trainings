for x in range(1,6):
	print(x)
num =list(range(6))
print(num)

num =list(range(2,11,2))
print(num)

squares=[]
for x in range(1,11):
	square = x ** 2
	squares.append(square)
print(squares)


squares=[]
for x in range(1,11):
	squares.append(x ** 2)
print(squares)

squares =[x**2 for x in range(1,11)]
print(squares)

#120P Exercise
for x in range(1,21):
	print(x)

calc = list(range(1,1000001))
print(max(calc))
print(min(calc))
print(sum(calc))

for x in range(1,20,2):
	print(x)

i=[]
for x in range(11):
	i.append(x*3)
print(i)

i=[]
for x in range(11):
	i.append(x**3)
print(i)

i = [x ** 3 for x in range(11)]
print(i)