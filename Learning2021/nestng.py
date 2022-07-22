alien = []
for i  in range(30):
 	new = {'clr':"green",'pnts':5,'sped':'slow'}
 	alien.append(new)

for alie in alien[:3]:
	if alie['clr'] == 'green':
		alie['clr'] = 'yellow'
		alie['pnts'] = 10
		alie['sped'] = 'medium'

	if alie['clr'] == 'yellow':
		alie['clr'] = 'red'
		alie['pnts'] ='15'
		alie['sped'] ='fast'
for a in alien[:5]:
	print(a)
print('......')

print('total number of alien ',len(alien))

v =[]
for i in range(20):
	m = 'vik'
	v.append(m)
print(v) 

menu = {
	'dosa':'roast',
	'sd':['cchut','spicychut']
	}
print(f"your order is {menu['dosa']} ")
for i in menu['sd']:
	print(f" {i}")

print('\n')

frnds ={
	'sarah' : ['python'],
	'vig':['python','MySQL'],
	'dhi':['c++',"c"]
	}

for n , l in frnds.items():
	print(f"{n.title()} favorite languages are")
	for i in l:
		print(f'\t {i}')

hi  ={
	'vik':{
		"first" : 'viky',
		'last' : 'siva',
		'location':'pyr',
		},
	}
for i,h in hi.items():
	print(f'username : {i}')
	fulln =(f"fullname = {h['first']} {h['last']}")
	location = (f"from = {h['location']}")
    
print(fulln.title())
print(location.upper()) 

