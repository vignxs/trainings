alien = {}
alien['clr'] = 'green'
alien['points'] = 5
print(alien)
alien['name'] = 'vignxs'
print(alien)
alien['clr'] = 'red'
print(alien)

alien={'x_position' : 0,'y_position' : 25, 'speed' : 'fast'}
print(f"the original speed of the alien is {alien['x_position']}")

if alien['speed'] == 'slow':
	x = 1
elif  alien['speed'] == 'medium':
	x = 2
else:
	x = 3

alien['x_position'] = alien['x_position'] + x
print(f"New Position is {alien['x_position']}")




print(alien)
del alien['speed']

print(alien)


print('\n   \n   \n    \n     \n')

nms = {
	'vik' : 3,
	'aks' : 4,
	'dhi' : 'bot',
	'san' : 6,
	"aad" : 7,
	}
print(nms)
bot = nms['dhi'].title()
print(f'dhivya is a {bot}')

print('\n   \n   \n    \n     \n')


alien={'x_position' : 0,'y_position' : 25, 'speed' : 'fast',"points":5}
point=alien.get('points',"no values")
print(point)
print(alien['points'])o