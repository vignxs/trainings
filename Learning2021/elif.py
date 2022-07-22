age = 16

if age < 4 :
	price = 0
elif age < 18 :
	price = 20
else :
	price = 60
print(f"the price {price} for you")

#150
alien_clr = ['green','blue','red']
for c in alien_clr[:3]:
	if c == 'green':
		print('you\'ve got 5 points')
	else:
		print('sry man')
		
clr = 'green'
if  clr == 'green':
	print('20 points')
else:
	print('no points')

c =list(range(1,1000001))
print(sum(c))

age = 3
if age <= 2 :
	print("baby")
elif age <= 4:
	print("toddler")

ppl = ['dhi','san','aad','adi']

if 'dhi' in ppl:
	print('you\'re the  best')

if 'san' in ppl:
	print("you're the strongest")

hi =[]
if hi:
	for h in hi:
		print('goood sir')
	print('well')
else:
	print('really')		