nms = ["viky",'dhi','san',"aad","aak"]
print(nms[0:3])
print(nms[::-1])
print(nms[2:4])
print(nms[3:])
print(nms[:3])
print(nms[-3:])
for x in nms[:3]:
	print(x)
names = nms[:]
print(names)
nms.append('adi')
names.append('d')
print(nms)
print(names)

print(names[:3])
print(names[2:-2])
print(names[-3:])

food =['idly','dosa','chut']
foods =food[:]
food.append('putchut')
foods.append('getchut')
for f in food:
	print(f)
print("\n")
for x in foods:
	print(x)
