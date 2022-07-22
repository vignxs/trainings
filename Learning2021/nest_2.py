hi = {
	'vik':['pyr','tqbr'],
	'dhi':['che','aadi'],
}
for i , v in hi.items():
	print(f"Name : {i}")

	for l in v:
		print(f"{l}")

nms = {
	'pyr': {
		'tmpl' : 'ganapathi temple',
		'rvr' : 'kattaru',
		'grassland':'several',
		}
	}
for i , v in nms.items():
	print(f"my home town is {i.upper()}")

	print(f"it has {v['grassland']} grasslands")
	print(f"we have {v['tmpl'].title()} around here")
	print(f"and specially we have {v['rvr'].title()} river")


hi=[]
for i in range(10):
	new ={'st':'mela thoppu','town':'pyr'}
	hi.append(new)
print(hi) 

hi=input()
print(hi)


hi = "'quit' or word"
h=""
while h != 'quit':
	h = input(hi)
	print(h)

